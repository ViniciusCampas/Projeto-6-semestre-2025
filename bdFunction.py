def insert(cursor, savedatabese):
    cursor.executemany(''' 
        INSERT INTO dados(
            nome,
            dataCriacao,
            dataExecucao,
            status,
            descricao
        ) VALUES(?,?,?,?,?)
    ''', savedatabese)

def select(cursor):
    cursor.execute('SELECT * FROM dados')
    rows = cursor.fetchall()
    return [dict(row) for row in rows]

def selectId(cursor, id):
    cursor.execute('SELECT * FROM dados WHERE id = ?', (id,))
    rows = cursor.fetchall()
    return [dict(row) for row in rows]

def delete(cursor, id):
    cursor.execute('DELETE FROM dados WHERE id = ?', (id,))

def update(cursor, savedatabese, id):
    cursor.execute('''
        UPDATE dados SET 
            nome= ?,
            dataCriacao=?,
            dataExecucao=?,
            status=?,
            descricao=?
        WHERE id = ?
    ''', (*savedatabese, id))
