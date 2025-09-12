#faz a leitura e determina a prioridade
def read(task):
    print('='*7,'Alta','='*7)
    for tas in task:
        if tas['Prioridade']=='alta':
            for key, value in tas.items():
                print(f'{key}:{value}')

    print('='*7,'Media','='*7)
    for tas in task:
        if tas['Prioridade']=='media':
            for key, value in tas.items():
                print(f'{key}:{value}')

    print('='*7,'Baixa','='*7)
    for tas in task:
        if tas['Prioridade']=='baixa':
            for key, value in tas.items():
                print(f'{key}:{value}')