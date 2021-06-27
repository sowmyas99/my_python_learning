import mysql.connector
import pytest

@pytest.fixture
def db_connection():
    conn=mysql.connector.connect(host="localhost", user = "xxxx",passwd = "xxxx", database = "DB1")
    return conn
