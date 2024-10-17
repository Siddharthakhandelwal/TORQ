import sqlite3


def ping():
    print('working ..')


def getAllData(sqlString, path):
    db = sqlite3.connect(path, uri=True)
    cur = db.cursor()
    cur.execute(sqlString)
    return cur.fetchall()


def crud(sqlString, path):
    db = sqlite3.connect(path)
    c = db.cursor()
    c.execute(sqlString)
    db.commit()
    db.close()