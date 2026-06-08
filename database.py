from dotenv import load_dotenv
from sshtunnel import SSHTunnelForwarder

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

import os

load_dotenv()

PA_USERNAME = os.getenv("PYTHONANYWHERE_USERNAME")
PA_PASSWORD = os.getenv("PYTHONANYWHERE_PASSWORD")

DB_USERNAME = os.getenv("MYSQL_USERNAME")
DB_PASSWORD = os.getenv("MYSQL_PASSWORD")
DB_HOST = os.getenv("MYSQL_HOST")
DB_NAME = os.getenv("MYSQL_DATABASE")

# Create SSH tunnel
tunnel = SSHTunnelForwarder(
    ("ssh.pythonanywhere.com"),
    ssh_username=PA_USERNAME,
    ssh_password=PA_PASSWORD,
    remote_bind_address=(DB_HOST, 3306)
)

tunnel.start()

DATABASE_URL = (
    f"mysql+pymysql://"
    f"{DB_USERNAME}:"
    f"{DB_PASSWORD}@"
    f"127.0.0.1:{tunnel.local_bind_port}/"
    f"{DB_NAME}"
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()