import logging
import azure.functions as func
import psycopg2
import os
from datetime import datetime
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *


def main(msg: func.ServiceBusMessage):

    notification_id = int(msg.get_body().decode('utf-8'))
    logging.info(
        f"Python ServiceBus queue trigger processed message: {str(notification_id)}")

    # Get connection to database
    conn = psycopg2.connect(
        host=os.environ["POSTGRES_URL"],
        database=os.environ["POSTGRES_DB"],
        user=os.environ["POSTGRES_USER"],
        password=os.environ["POSTGRES_PW"]
    )
    logging.info(f"Successfully connected to database")

    try:
        # Get notification message and subject from database using the notification_id
        cursor = conn.cursor()
        cmd = f"SELECT message, subject FROM notification WHERE id={str(notification_id)}"
        cursor.execute(cmd)
        logging.info(
            f"Notification ID {str(notification_id)}: Get message and subject")

        for row in cursor.fetchall():
            message = row[0]
            subject = row[1]

        if not message or not subject:
            error_message = f"Notification ID {str(notification_id)}: No message or subject"
            logging.error(error_message)
            raise Exception(error_message)

        logging.info(
            f"Notification ID {str(notification_id)}: Message '{message}', Subject '{subject}'")

        # Get attendees email and name
        cmd = f"SELECT first_name, last_name, email FROM attendee"
        cursor.execute(cmd)
        count = 0

        # Loop through each attendee and send an email with a personalized subject
        for row in cursor.fetchall():
            first_name = row[0]
            last_name = row[1]
            email = row[2]

            logging.info(
                f"Notification ID {str(notification_id)}: First name '{first_name}', last name '{last_name}', email '{email}'")

            from_email = Email(os.environ['ADMIN_EMAIL_ADDRESS'])
            to_emails = To(email)
            personalized_subject = f"Hello, {first_name}! {subject}"
            content = Content("text/plain", message)

            logging.info(f"Sendgrid API key {os.environ['SENDGRID_API_KEY']}")

            mail = Mail(from_email, to_emails, personalized_subject, content)
            sg = SendGridAPIClient(os.environ['SENDGRID_API_KEY'])
            sg.send(mail)

            count += 1

        # Update the notification table by setting the completed date and
        # updating the status with the total number of attendees notified
        status = f"Notified {str(count)} attendees"
        date = datetime.now()
        logging.info(f"Notification ID {str(notification_id)}: {status}@{date}")

        cmd = f"UPDATE notification SET status='{status}' WHERE id={str(notification_id)}"
        cursor.execute(cmd)

        cmd = f"UPDATE notification SET completed_date='{str(date)}' WHERE id={str(notification_id)}"
        cursor.execute(cmd)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)
    finally:
        # Close connection
        conn.close()