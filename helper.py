import mysql.connector
import pandas as pd


def sqltopd(sql, db):
    cursorref = db.cursor()
    cursorref.execute(sql)
    return pd.DataFrame(cursorref.fetchall())


def getConnector(server,user,password,db):
    return mysql.connector.connect(
        host=server,
        user=user,
        password=password,
        database=db
    )
