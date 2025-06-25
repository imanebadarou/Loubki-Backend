from db import get_db

@staticmethod
def list_items():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM item")
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    return [dict(zip(columns, row)) for row in rows]

@staticmethod
def list_required_items(choice_id):
    cur = get_db().cursor()
    cur.execute("SELECT item.id, item.label, required.quantity, required.lose_item FROM item JOIN required ON item.id=required.item_id JOIN choice ON choice.id=required.choice_id WHERE choice.id=?", (choice_id,))
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    return [dict(zip(columns, row)) for row in rows]

@staticmethod
def list_items_received(chapter_id):
    cur = get_db().cursor()
    cur.execute("SELECT item.id, item.label, receive.quantity, chapter.id, chapter.name FROM item JOIN receive ON item.id=receive.item_id JOIN chapter ON chapter.id=receive.chapter_id WHERE chapter.id=?",(chapter_id,))
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    return [dict(zip(columns, row)) for row in rows]