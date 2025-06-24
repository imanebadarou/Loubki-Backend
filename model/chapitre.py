from db import get_db

@staticmethod
def list_chap(id_hist):
    cur = get_db().cursor()
    cur.execute("SELECT id_chap, nom_chap, contenu_chap FROM chapitre WHERE id_hist=?", (id_hist,))
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    return [dict(zip(columns, row)) for row in rows]

