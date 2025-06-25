from db import get_db

# SELECT

@staticmethod
def list_stories():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM story")
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    return [dict(zip(columns, row)) for row in rows]

@staticmethod
def get_story(id):
    cur = get_db().cursor()
    cur.execute('SELECT * FROM story WHERE id=?',(id,))
    columns = [desc[0] for desc in cur.description]
    row = cur.fetchone()
    return dict(zip(columns, row))

# CREATE

@staticmethod
def create_story(data):
    cur = get_db().cursor()
    cur.execute('INSERT INTO story (name, img_url, description) VALUES (?, ?, ?)',
                (data['name'], data['img_url'], data['description']))
    get_db().commit()
    return

# UPDATE

@staticmethod
def update_story(id, data):
    cur = get_db().cursor()
    fields = []
    values = []
    for key in ['name', 'img_url', 'description']:
        if key in data:
            fields.append(f"{key}=?")
            values.append(data[key])
    if not fields:
        return  # Nothing to update
    values.append(id)
    sql = f"UPDATE story SET {', '.join(fields)} WHERE id=?"
    cur.execute(sql, values)
    get_db().commit()
    return

# DELETE

@staticmethod
def delete_story(id):
    cur = get_db().cursor()
    cur.execute('DELETE FROM story WHERE id=?', (id,))
    get_db().commit()
    return