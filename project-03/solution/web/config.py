import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = True
    PORT: int(8000)
    POSTGRES_URL = 'yross-postgres-server.postgres.database.azure.com'
    POSTGRES_USER = 'yrosspostgres@yross-postgres-server' 
    POSTGRES_PW = '0#LPtMEeCo' 
    POSTGRES_DB = 'techconfdb' 
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY = 'LWd2tzlprdGHCIPHTd4tp5SBFgDszm'
    SERVICE_BUS_CONNECTION_STRING = 'Endpoint=sb://yross-service-bus-1.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=oGRzfDxnT2Hm7vWaDSfbEKFCM/TVLkyQ2pNFaFeN+cY='
    SERVICE_BUS_QUEUE_NAME = 'notificationqueue'
    ADMIN_EMAIL_ADDRESS = 'ythalorossy@gmail.com'
    SENDGRID_API_KEY = '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' #Configuration not required, required SendGrid Account

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False