import os

## DATABASE_CONFIG 
DATABASE_NAME = os.environ.get('DATABASE_NAME','Not Set Name Database')
DATABASE_HOST_CONNECT= os.environ.get('DATABASE_HOST','Not Set Host Connect')
DATABASE_USER = os.environ.get('DATABASE_USER', 'Not Set  User ')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD', 'Not Set Password Database')
DATABASE_PORT = os.environ.get('DATABASE_PORT', 'Not Set Port Database')


### PATH CSV
PATH_CSV = os.environ.get('PATH_CSV', 'NOT SET PATH CSV')
NAME_ARCHIVE_CSV = os.environ.get('NAME_CSV', 'NOT SET NAME ARCHIVE CSV')



#### MONGO DB URL CONFIG
URL_MONGO_DB = os.environ.get('URL_MONGO_DB', 'NOT SET URL MONGODB')


