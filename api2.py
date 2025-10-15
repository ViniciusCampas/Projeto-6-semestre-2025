from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {
    "Nome": "teste3",
    "Data Inicial": "09/29/25/26/2025 - 12:26:20",
    "Data final": "10/10/2025",
    "Prioridade": "Baixa",
    "Sobre": "teste3teste3teste3teste3teste3teste3"
  }
]

@app.route('/tasks',methods=['POST'])
def teste():
    teste=request.get_json()
    return jsonify(teste)

#falta testar

app.run(debug=True)