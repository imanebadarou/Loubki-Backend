from db import get_db

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
        JOIN chapter next_chapter ON choice.id = next_chapter.prev_choice_id
        WHERE id=?""", 
        (id,)
    )
    columns = [desc[0] for desc in cur.description]
    row = cur.fetchone()
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