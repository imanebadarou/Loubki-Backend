from db import get_db

@staticmethod
def list_choices():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM choice")
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

@staticmethod
def list_chapter_choices(chapter_id):
    cur = get_db().cursor()
    cur.execute('SELECT choice.content, choice.id, choice.prev_chapter_id, choice.next_chapter_id FROM choice JOIN chapter ON choice.prev_chapter_id = chapter.id WHERE chapter.id=?', (chapter_id,))
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    return [dict(zip(columns, row)) for row in rows]