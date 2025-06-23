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
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    return [dict(zip(columns, row)) for row in rows]

def histoire_id(id):
    cur = get_db().cursor()
    cur.execute('SELECT * FROM histoire WHERE id_hist=?',(id,))
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    return [dict(zip(columns, row)) for row in rows]

def histoire_choix(id):
    cur = get_db().cursor()
    cur.execute('SELECT id_choix, txt_choix, chap_prev, chap_next FROM choix JOIN chapitre ON choix.chap_prev = chapitre.id_chap WHERE chapitre.id_hist=?',(id,))
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    return [dict(zip(columns, row)) for row in rows]

def list_choix():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM choix")
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    return [dict(zip(columns, row)) for row in rows]

def choix_id(id):
    cur = get_db().cursor()
    cur.execute('SELECT * FROM choix WHERE id_hist=?',(id,))
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    return [dict(zip(columns, row)) for row in rows]


def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

