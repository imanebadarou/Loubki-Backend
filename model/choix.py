from db import get_db

@staticmethod
def list_choix():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM choix")
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    return [dict(zip(columns, row)) for row in rows]

@staticmethod
def choix_id(id):
    cur = get_db().cursor()
    cur.execute('SELECT * FROM choix WHERE id_choix=?',(id,))
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    return [dict(zip(columns, row)) for row in rows]

@staticmethod
def choix_chap(id_hist, id_chap):
    cur = get_db().cursor()
    cur.execute('SELECT id_choix, txt_choix FROM choix JOIN chapitre ON choix.chap_prev = id_chap WHERE id_hist=? AND id_chap=?',(id_hist,id_chap))
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    return [dict(zip(columns, row)) for row in rows]