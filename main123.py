import requests as rq

tasks = [
  {
    "Nome": "teste5",
    "Data Inicial": "10/29/25/26/2025 - 12:26:20",
    "Data final": "11/11/2025",
    "Prioridade": "nada",
    "Sobre": "teste5teste5teste5"
  }]
b=rq.post('http://localhost:5000/tasks',json=tasks)
a= rq.get('http://localhost:5000/tasks')

print (a.text)
