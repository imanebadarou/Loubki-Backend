from db import get_db

@staticmethod
def list_chapters(story_id=None):
    cur = get_db().cursor()
    cur.execute("SELECT * FROM chapter WHERE story_id=?", (story_id,))
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    return [dict(zip(columns, row)) for row in rows]

@staticmethod
def get_chapter(id):
    cur = get_db().cursor()
    cur.execute("SELECT * FROM chapter WHERE chapter_id=?", (id))
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    return [dict(zip(columns, row)) for row in rows]
