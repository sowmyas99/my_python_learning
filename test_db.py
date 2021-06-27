import pytest

def test_database(db_connection):
    cur=db_connection.cursor()
    sql="select * from Employee"
    cur.execute(sql)
    rs = cur.fetchall()
    assert len(rs) == 1