from db import get_db

# SELECT

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
    print(type(id))
    cur.execute("SELECT * FROM chapter WHERE id=?", (id,))
    columns = [desc[0] for desc in cur.description]
    row = cur.fetchone()
    return dict(zip(columns, row))

# CREATE

@staticmethod
def create_chapter(data):
    db = get_db()
    cur = db.cursor()
    cur.execute(
        "INSERT INTO chapter (story_id, title, content) VALUES (?, ?, ?)",
        (data["story_id"], data["title"], data["content"])
    )
    db.commit()
    return cur.lastrowid

@staticmethod
def update_chapter(id, data):
    db = get_db()
    cur = db.cursor()
    fields = []
    values = []
    if "title" in data:
        fields.append("title=?")
        values.append(data["title"])
    if "content" in data:
        fields.append("content=?")
        values.append(data["content"])
    values.append(id)
    if fields:
        cur.execute(
            f"UPDATE chapter SET {', '.join(fields)} WHERE id=?",
            tuple(values)
        )
        db.commit()
        return cur.rowcount
    return 0

@staticmethod
def delete_chapter(id):
    db = get_db()
    cur = db.cursor()
    cur.execute("DELETE FROM chapter WHERE id=?", (id,))
    db.commit()
    return cur.rowcount