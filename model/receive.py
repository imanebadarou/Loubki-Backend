from db import get_db

# CREATE

@staticmethod
def get_receive(item_id, chapter_id):
    cur = get_db().cursor()
    cur.execute("""
        SELECT item.label, receive.quantity, receive.chapter_id, receive.item_id, receive.quantity 
        FROM receive 
        JOIN item ON item.id == receive.item_id 
        WHERE item_id=? AND chapter_id=?""", 
        (item_id, chapter_id)
    )
    columns = [desc[0] for desc in cur.description]
    row = cur.fetchone()
    return dict(zip(columns, row))

@staticmethod
def create_receive(data):
    cur = get_db().cursor()
    cur.execute('INSERT INTO receive (item_id, chapter_id, quantity) VALUES (?, ?, ?)', (data['item_id'], data['chapter_id'], data['quantity']))
    get_db().commit()
    return data['chapter_id'], data['item_id']

# UPDATE

@staticmethod
def update_receive(item_id, chapter_id, data):
    cur = get_db().cursor()
    fields = []
    values = []
    for key in ['quantity']:
        if key in data:
            fields.append(f"{key}=?")
            values.append(data[key])
    if not fields:
        return  # Nothing to update
    values.append(item_id)
    values.append(chapter_id)
    sql = f"UPDATE receive SET {', '.join(fields)} WHERE item_id=? AND chapter_id=?"
    cur.execute(sql, values)
    get_db().commit()
    return cur.rowcount > 0

# DELETE

@staticmethod
def delete_receive(item_id, chapter_id):
    cur = get_db().cursor()
    cur.execute('DELETE FROM receive WHERE item_id=? AND chapter_id=?', (item_id, chapter_id))
    get_db().commit()
    return cur.rowcount > 0