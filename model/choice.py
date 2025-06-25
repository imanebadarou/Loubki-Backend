from db import get_db

# SELECT

@staticmethod
def list_choices(story_id):
    cur = get_db().cursor()
    cur.execute("""
        SELECT choice.content, choice.id, choice.prev_chapter_id, next_chapter.id AS next_chapter_id
        FROM choice
        JOIN chapter next_chapter ON choice.id = next_chapter.prev_choice_id
        JOIN story ON next_chapter.story_id = story.id
        WHERE story.id=?""", 
    (story_id,))
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    return [dict(zip(columns, row)) for row in rows]

@staticmethod
def get_choice(id):
    cur = get_db().cursor()
    cur.execute("""
        SELECT choice.content, choice.id, choice.prev_chapter_id, next_chapter.id AS next_chapter_id
        FROM choice 
        LEFT JOIN chapter next_chapter ON choice.id = next_chapter.prev_choice_id
        WHERE choice.id=?""", 
        (id,)
    )
    columns = [desc[0] for desc in cur.description]
    row = cur.fetchone()
    print("ICI")
    print(id)
    print(row)
    return dict(zip(columns, row))

@staticmethod
def list_chapter_choices(chapter_id):
    cur = get_db().cursor()
    cur.execute("""
        SELECT choice.content, choice.id, choice.prev_chapter_id, next_chapter.id AS next_chapter_id
        FROM choice
        LEFT JOIN chapter next_chapter ON choice.id = next_chapter.prev_choice_id
        WHERE choice.prev_chapter_id=?
    """, (chapter_id,))
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    return [dict(zip(columns, row)) for row in rows]

# CREATE

@staticmethod
def create_choice(data):
    db = get_db()
    cur = db.cursor()
    cur.execute(
        "INSERT INTO choice (content, prev_chapter_id) VALUES (?, ?)",
        (data['content'], data['prev_chapter_id'])
    )
    db.commit()
    return cur.lastrowid

@staticmethod
def update_choice(choice_id, content=None, prev_chapter_id=None):
    db = get_db()
    cur = db.cursor()
    fields = []
    values = []
    if content is not None:
        fields.append("content=?")
        values.append(content)
    if prev_chapter_id is not None:
        fields.append("prev_chapter_id=?")
        values.append(prev_chapter_id)
    values.append(choice_id)
    cur.execute(
        f"UPDATE choice SET {', '.join(fields)} WHERE id=?",
        values
    )
    db.commit()
    return cur.rowcount > 0

@staticmethod
def delete_choice(choice_id):
    db = get_db()
    cur = db.cursor()
    cur.execute("DELETE FROM choice WHERE id=?", (choice_id,))
    db.commit()
    return cur.rowcount > 0