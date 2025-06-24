from db import get_db

@staticmethod
def list_obj():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM objet")
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    return [dict(zip(columns, row)) for row in rows]

@staticmethod
def obj_requis():
    cur = get_db().cursor()
    cur.execute("SELECT O.id_obj, O.nom_obj, R.quantite, R.perd_obj, C.id_choix, C.txt_choix FROM objet O JOIN requis R ON O.id_obj=R.id_obj JOIN choix C ON C.id_choix=R.id_choix")
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    return [dict(zip(columns, row)) for row in rows]

@staticmethod
def obj_requis_choix(id_choix):
    cur = get_db().cursor()
    cur.execute("SELECT O.id_obj, O.nom_obj, R.quantite, R.perd_obj FROM objet O JOIN requis R ON O.id_obj=R.id_obj JOIN choix C ON C.id_choix=R.id_choix WHERE C.id_choix=?", (id_choix,))
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    return [dict(zip(columns, row)) for row in rows]

@staticmethod
def obj_obtenus():
    cur = get_db().cursor()
    cur.execute("SELECT Obj.id_obj, Obj.nom_obj, O.quantite, C.id_chap, C.nom_chap FROM objet Obj JOIN obtenir O ON Obj.id_obj=O.id_obj JOIN chapitre C ON C.id_chap=O.id_chap")
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    return [dict(zip(columns, row)) for row in rows]

@staticmethod
def obj_obtenu_chap(id_chap):
    cur = get_db().cursor()
    cur.execute("SELECT Obj.id_obj, Obj.nom_obj, O.quantite, C.id_chap, C.nom_chap FROM objet Obj JOIN obtenir O ON Obj.id_obj=O.id_obj JOIN chapitre C ON C.id_chap=O.id_chap WHERE C.id_chap=?",(id_chap,))
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    return [dict(zip(columns, row)) for row in rows]