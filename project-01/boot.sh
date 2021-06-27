#!/bin/bash

echo "Setting the environment variables"

export BLOB_ACCOUNT='yross01'
export BLOB_STORAGE_KEY='RHD3rZJMQ13zDdRkZv/jO4RUCUPEGYcXPWUP9gLie39AVw2hxm1y7WMnY7S1OSjcKeQFbrhPVDYJVjPkL3fGtQ=='
export BLOB_CONTAINER='images'
export SQL_SERVER='yross-sql-server.database.windows.net'
export SQL_DATABASE='yross-sql-database'
export SQL_USER_NAME='yross'
export SQL_PASSWORD='my-passw0rd-(!)'

export CLIENT_ID='f71716cb-55e0-4636-a62c-c0cda7e08a3c'
export CLIENT_SECRET='LS3.X1_PJIcHh_.69O954GOX53CzCcMaqm'
export REDIRECT_PATH='/getAToken'

echo "Environment variables setup finished"

echo " "

echo "Booting the Application"
python3 application.py