from db import get_db

@staticmethod
def list_choices():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM choices")
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    return [dict(zip(columns, row)) for row in rows]

@staticmethod
def get_choice(id):
    cur = get_db().cursor()
    cur.execute('SELECT * FROM choice WHERE id_choix=?', (id,))
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    return [dict(zip(columns, row)) for row in rows]