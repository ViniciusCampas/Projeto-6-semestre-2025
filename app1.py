from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
  {
    "Nome": "teste1",
    "Data Inicial": "09/29/25/26/2025 - 12:26:20",
    "Data final": "10/10/2025",
    "Prioridade": "Alta",
    "Sobre": "teste1teste1teste1teste1teste1teste1"
  },
    {
    "Nome": "teste2",
    "Data Inicial": "09/29/25/26/2025 - 12:26:20",
    "Data final": "10/10/2025",
    "Prioridade": "Media",
    "Sobre": "teste2teste2teste2teste2teste2teste2"
  },
    {
    "Nome": "teste3",
    "Data Inicial": "09/29/25/26/2025 - 12:26:20",
    "Data final": "10/10/2025",
    "Prioridade": "Baixa",
    "Sobre": "teste3teste3teste3teste3teste3teste3"
  }
]

# Consultar(todos)
@app.route('/tasks',methods=['GET'])
def getTask():
    return jsonify(tasks)

# Consultar(id)
@app.route('/tasks/<int:id>',methods=['GET'])
def getTaskId(id):
    for task in tasks:
        if task.get('id') == id:
            return jsonify(task)
# Editar
@app.route('/tasks/<int:id>',methods=['PUT'])
def updateTask(id):
    alterTask = request.get_json()
    for indice,livro in enumerate(tasks):
        if livro.get('id') == id:
            tasks[indice].update(alterTask)
            return jsonify(tasks[indice])
# Criar
@app.route('/tasks',methods=['POST'])
def createTask():
    newTask = request.get_json()
    tasks.append(newTask)
   
    return jsonify(tasks)
# Excluir
@app.route('/tasks/<int:id>',methods=['DELETE'])
def deletTask(id):
    for indice, task in enumerate(tasks):
        if task.get('id') == id:
            del tasks[indice]

    return jsonify(tasks)

app.run(port=5000,host='localhost',debug=True)
