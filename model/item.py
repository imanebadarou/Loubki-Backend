from db import get_db

# SELECT

@staticmethod
def list_items():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM item")
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    return [dict(zip(columns, row)) for row in rows]

@staticmethod
def get_item(id):
    cur = get_db().cursor()
    cur.execute('SELECT * FROM item WHERE id=?',(id,))
    columns = [desc[0] for desc in cur.description]
    row = cur.fetchone()
    return dict(zip(columns, row))

@staticmethod
def list_required_items(choice_id):
    cur = get_db().cursor()
    cur.execute("SELECT item.label, required.quantity, required.item_id, required.choice_id, required.lose_item FROM item JOIN required ON item.id=required.item_id JOIN choice ON choice.id=required.choice_id WHERE choice.id=?", (choice_id,))
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    return [dict(zip(columns, row)) for row in rows]

@staticmethod
def list_items_received(chapter_id):
    cur = get_db().cursor()
    cur.execute("SELECT item.label, receive.quantity, receive.chapter_id, receive.item_id FROM item JOIN receive ON item.id=receive.item_id JOIN chapter ON chapter.id=receive.chapter_id WHERE chapter.id=?",(chapter_id,))
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    return [dict(zip(columns, row)) for row in rows]

# CREATE

@staticmethod
def create_item(data):
    cur = get_db().cursor()
    cur.execute('INSERT INTO item (label) VALUES (?)', (data['label'],))
    get_db().commit()
    return cur.lastrowid

# UPDATE

@staticmethod
def update_item(id, data):
    cur = get_db().cursor()
    fields = []
    values = []
    for key in ['label']:
        if key in data:
            fields.append(f"{key}=?")
            values.append(data[key])
    if not fields:
        return  # Nothing to update
    values.append(id)
    sql = f"UPDATE item SET {', '.join(fields)} WHERE id=?"
    cur.execute(sql, values)
    get_db().commit()
    return

# DELETE

@staticmethod
def delete_item(id):
    cur = get_db().cursor()
    cur.execute('DELETE FROM item WHERE id=?', (id,))
    get_db().commit()
    return