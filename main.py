# -*- coding: utf-8 -*-
import requests as rq

def imprimir(task):
    for tas in task:
        print(f'id : {tas['id']}')
        print(f'nome : {tas['nome']}')
        print(f'dataCriacao : {tas['dataCriacao']}')
        print(f'dataExecucao : {tas['dataExecucao']}')
        print(f'status : {tas['status']}')
        print(f'descricao : {tas['descricao']}')
        print('*'*100)

tasks = [
 
  {
    'nome': 'Revisar proposta comercial',
    'dataCriacao': '2025-10-28',
    'dataExecucao': '2025-11-01',
    'status': 'pendente',
    'descricao': 'Verificar detalhes do orçamento e ajustar valores antes do envio final.'
  },
  {
    'nome': 'Organizar arquivos da equipe',
    'dataCriacao': '2025-11-02',
    'dataExecucao': '2025-11-06',
    'status': 'pendente',
    'descricao': 'Separar documentos antigos e criar pastas novas no drive.'
  },
  {
    'nome': 'Responder e-mails pendentes',
    'dataCriacao': '2025-11-05',
    'dataExecucao': '2025-11-05',
    'status': 'pendente',
    'descricao': 'Dar retorno aos clientes que aguardam resposta desde a última semana.'
  },
  {
    'nome': 'Atualizar planilha de despesas',
    'dataCriacao': '2025-11-08',
    'dataExecucao': '2025-11-09',
    'status': 'pendente',
    'descricao': 'Adicionar gastos recentes e revisar totais.'
  },
  {
    'nome': 'Reunião com o setor de marketing',
    'dataCriacao': '2025-11-09',
    'dataExecucao': '2025-11-12',
    'status': 'pendente',
    'descricao': 'Discutir próximos passos da campanha de fim de ano.'
  },
  {
    'nome': 'Fazer backup dos projetos',
    'dataCriacao': '2025-11-10',
    'dataExecucao': '2025-11-13',
    'status': 'pendente',
    'descricao': 'Garantir que todos os arquivos estejam salvos no servidor.'
  },
  {
    'nome': 'Agendar check-up médico',
    'dataCriacao': '2025-11-11',
    'dataExecucao': '2025-11-20',
    'status': 'pendente',
    'descricao': 'Lembrar de marcar consulta antes do final do mês.'
  },
  {
    'nome': ' Revisar apresentação do projeto',
    'dataCriacao': '2025-11-12',
    'dataExecucao': '2025-11-15',
    'status': 'pendente',
    'descricao': 'Dar uma última olhada no material e ajustar slides.'
  },
  {
    'nome': 'Ler relatórios da concorrência',
    'dataCriacao': '2025-11-10',
    'dataExecucao': '2025-11-17',
    'status': 'pendente',
    'descricao': 'Analisar tendências e estratégias usadas por empresas similares. '
  },
  {
    'nome': 'Planejar postagens da semana',
    'dataCriacao': '2025-11-07',
    'dataExecucao': '2025-11-10',
    'status': 'pendente',
    'descricao': 'Montar calendário com ideias para redes sociais.'
  }
]

salvar=rq.post('http://localhost:5000/tasks',json=tasks)

consultar= rq.get('http://localhost:5000/tasks')

print ('PRIMEIRA CONSULTA')
print('='*100)
imprimir (consultar.json())
print('='*100)

consutarID= rq.get('http://localhost:5000/tasks/3')

print ('CONSULTA POR ID')
print('='*100)

imprimir (consutarID.json())
print('='*100)

tasksAlterada = {
    'nome': 'Desorganizar Tudo',
    'dataCriacao': '2025-11-12',
    'dataExecucao': '2025-11-20',
    'status': 'pendente',
    'descricao': 'Bagunçar todos os arquivos .'
  }
  

alterar=rq.put('http://localhost:5000/tasks/2',json=tasksAlterada)

consultar= rq.get('http://localhost:5000/tasks')

print ('CONSULTA DE ALTERAÇÃO')
print('='*100)
imprimir (consultar.json())
print('='*100)

deletar =rq.delete('http://localhost:5000/tasks/1')

consultar= rq.get('http://localhost:5000/tasks')

print ('CONSULTA DELETE')
print('='*100)
imprimir (consultar.json())
print('='*100)
