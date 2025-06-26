from db import get_db

# CREATE

@staticmethod
def get_required(item_id, choice_id):
    cur = get_db().cursor()
    cur.execute("""
        SELECT item.id, item.label, required.quantity, required.choice_id, required.item_id, required.quantity, required.lose_item
        FROM required
        JOIN item ON item.id == required.item_id
        WHERE item_id=? AND choice_id=?
    """, (item_id, choice_id))
    columns = [desc[0] for desc in cur.description]
    row = cur.fetchone()
    if row:
        return dict(zip(columns, row))

@staticmethod
def create_required(data):
    cur = get_db().cursor()
    cur.execute('INSERT INTO required (item_id, choice_id, quantity, lose_item) VALUES (?, ?, ?, ?)', (data['item_id'], data['choice_id'], data['quantity'], data['lose_item']))
    get_db().commit()
    return data['choice_id'], data['item_id']

# UPDATE

@staticmethod
def update_required(item_id, choice_id, data):
    cur = get_db().cursor()
    fields = []
    values = []
    for key in ['quantity', 'lose_item']:
        if key in data:
            fields.append(f"{key}=?")
            values.append(data[key])
    if not fields:
        return  # Nothing to update
    values.append(item_id)
    values.append(choice_id)
    sql = f"UPDATE required SET {', '.join(fields)} WHERE item_id=? AND choice_id=?"
    cur.execute(sql, values)
    get_db().commit()
    return cur.rowcount > 0

# DELETE

@staticmethod
def delete_required(item_id, choice_id):
    cur = get_db().cursor()
    cur.execute('DELETE FROM required WHERE item_id=? AND choice_id=?', (item_id, choice_id))
    get_db().commit()
    return cur.rowcount > 0