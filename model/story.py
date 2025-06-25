from db import get_db

@staticmethod
def list_stories():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM story")
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    return [dict(zip(columns, row)) for row in rows]

@staticmethod
def get_story(id):
    cur = get_db().cursor()
    cur.execute('SELECT * FROM story WHERE id=?',(id,))
    columns = [desc[0] for desc in cur.description]
    row = cur.fetchall()
    return dict(zip(columns, row))

# @staticmethod
# def histoire_choix(id):
#     cur = get_db().cursor()
#     cur.execute('SELECT id_choix, txt_choix, chap_prev, chap_next FROM choix JOIN chapitre ON choix.chap_prev = chapitre.id_chap WHERE chapitre.id_hist=?',(id,))
#     columns = [desc[0] for desc in cur.description]
#     rows = cur.fetchall()
#     return [dict(zip(columns, row)) for row in rows]

# @staticmethod
# def hist_first_chap(id):
#     cur = get_db().cursor()
#     cur.execute('SELECT id_chap, nom_chap, contenu_chap FROM histoire H JOIN chapitre C ON H.first_chap_id=C.id_chap WHERE H.id_hist=?',(id,))
#     columns = [desc[0] for desc in cur.description]
#     rows = cur.fetchall()
#     return [dict(zip(columns, row)) for row in rows]