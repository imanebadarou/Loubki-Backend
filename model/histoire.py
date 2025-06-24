from db import get_db

@staticmethod
def list_histoires():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM histoire")
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    return [dict(zip(columns, row)) for row in rows]

@staticmethod
def histoire_id(id):
    cur = get_db().cursor()
    cur.execute('SELECT * FROM histoire WHERE id_hist=?',(id,))
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    return [dict(zip(columns, row)) for row in rows]

# @staticmethod
# def histoire_choix(id):
#     cur = get_db().cursor()
#     cur.execute('SELECT id_choix, txt_choix, chap_prev, chap_next FROM choix JOIN chapitre ON choix.chap_prev = chapitre.id_chap WHERE chapitre.id_hist=?',(id,))
#     columns = [desc[0] for desc in cur.description]
#     rows = cur.fetchall()
#     return [dict(zip(columns, row)) for row in rows]