import os
import urllib.parse

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")

    SQL_SERVER = os.environ.get("SQL_SERVER")
    SQL_DATABASE = os.environ.get("SQL_DATABASE")
    SQL_USERNAME = os.environ.get("SQL_USERNAME")
    SQL_PASSWORD = os.environ.get("SQL_PASSWORD")

    params = urllib.parse.quote_plus(
        f"Driver=ODBC Driver 18 for SQL Server;"
        f"Server={SQL_SERVER};"
        f"Database={SQL_DATABASE};"
        f"UID={SQL_USERNAME};"
        f"PWD={SQL_PASSWORD};"
        f"Encrypt=yes;"
        f"TrustServerCertificate=no;"
    )

    SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc:///?odbc_connect={params}"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get("BLOB_ACCOUNT")
    BLOB_KEY = os.environ.get("BLOB_KEY")
    BLOB_CONTAINER = os.environ.get("BLOB_CONTAINER")

    BLOB_CONNECTION_STRING = (
        f"DefaultEndpointsProtocol=https;"
        f"AccountName={BLOB_ACCOUNT};"
        f"AccountKey={BLOB_KEY};"
        f"EndpointSuffix=core.windows.net"
    )

