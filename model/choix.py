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
    cur.execute('SELECT * FROM choix WHERE id_hist=?',(id,))
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    return [dict(zip(columns, row)) for row in rows]

