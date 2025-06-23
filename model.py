from flask import g
import sqlite3

DATABASE = 'db/database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@staticmethod
def list_histoires():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM histoire")
    rows = cur.fetchall()
    return rows

def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()