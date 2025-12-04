from flask import Flask, jsonify, request
import sqlite3
import bdFunction 
import prioridade 

app = Flask(__name__)

DATABASE = 'dbaTasks.db'

def get_db_connection():
    conec = sqlite3.connect(DATABASE)
    conec.row_factory = sqlite3.Row
    return conec

def init_db():
    conec = get_db_connection()
    cursor = conec.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dados(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            dataCriacao TEXT NOT NULL,
            dataExecucao TEXT NOT NULL,
            status TEXT NOT NULL,
            descricao TEXT NOT NULL
        )
    ''')
    conec.commit()
    conec.close()

init_db()

@app.route('/tasks', methods=['GET'])
def getTask():
    conec = get_db_connection()
    cursor = conec.cursor()
    resultado = bdFunction.select(cursor)
    textos2=[]
    text=[]
    for t in resultado:
        text.append(f'{t['nome']},{t['descricao']}')

    textosPrioritizados = sorted(text, key=prioridade.classificarPrioridade, reverse=True)

    for textPri in textosPrioritizados:
        for te in resultado:
            if f'{te['nome']},{te['descricao']}'== textPri:
                textos2.append(te)
    conec.close()
    return jsonify(textos2)

@app.route('/tasks/<int:id>', methods=['GET'])
def getTaskId(id):
    conec = get_db_connection()
    cursor = conec.cursor()
    resultado = bdFunction.selectId(cursor, id)
    conec.close()
    return jsonify(resultado)

@app.route('/tasks/<int:id>', methods=['PUT'])
def updateTask(id):
    tasks2 = request.get_json()

    alterT = (
        tasks2.get('nome'),
        tasks2.get('dataCriacao'),
        tasks2.get('dataExecucao'),
        tasks2.get('status'),
        tasks2.get('descricao')
    )

    conec = get_db_connection()
    cursor = conec.cursor()
    bdFunction.update(cursor, alterT, id)
    conec.commit()
    resultado = bdFunction.selectId(cursor, id)
    conec.close()

    return jsonify(resultado)


@app.route('/tasks', methods=['POST'])
def createTask():
    newTask = request.get_json()

    savedatabese = [
        (mt['nome'], mt['dataCriacao'], mt['dataExecucao'], mt['status'], mt['descricao'])
        for mt in newTask
    ]

    conec = get_db_connection()
    cursor = conec.cursor()
    bdFunction.insert(cursor, savedatabese)
    conec.commit()
    resultado = bdFunction.select(cursor)
    conec.close()
    return jsonify(resultado), 201

@app.route('/tasks/<int:id>', methods=['DELETE'])
def deletTask(id):
    conec = get_db_connection()
    cursor = conec.cursor()
    bdFunction.delete(cursor, id)
    conec.commit()
    resultado = bdFunction.select(cursor)
    conec.close()
    return jsonify(resultado)


app.run(port=5000, host='localhost', debug=True)
