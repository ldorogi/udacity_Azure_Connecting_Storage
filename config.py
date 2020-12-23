import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'sql-server-dl.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'sql-database-dl'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'admin-dl'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'SystemCompakt68'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'storageaccountdl'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'B0IggbRioHNpizM8aBefES8tsAtT8Brpk2w/Fk3qLJcQqHr2BeEFTmfjijH5BIgppASfPLig5OdJ+gwEH8tImA=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
