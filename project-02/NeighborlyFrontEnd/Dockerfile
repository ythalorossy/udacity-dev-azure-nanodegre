# To enable ssh & remote debugging on app service change the base image to the one below
# FROM mcr.microsoft.com/azure-functions/python:3.0-python3.8-appservice
FROM mcr.microsoft.com/azure-functions/python:3.0-python3.8

ENV host:logger:consoleLoggingMode=always

# Add files from this repo to the root site folder.
COPY . /home/site/wwwroot

EXPOSE 8080

RUN /usr/local/bin/python -m pip install --upgrade pip

# Install requirements
RUN cd /home/site/wwwroot && pip install -r requirements.txt

ENV FLASK_RUN=app.py

WORKDIR /home/site/wwwroot

ENTRYPOINT [ "flask", "run" ]
