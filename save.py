import json
#abre o arquivo .json para leitura
def load(task,caminho):
    arr=[]
    try:
        with open (caminho,'r', encoding='utf-8') as arquivo:
            arr=json.load(arquivo)
        return arr
    except FileNotFoundError:
        print('Arquivo não existe')
        save(task,caminho)
        return arr
#abre o arquivo .json para escrita
def save(task,caminho):
    with open (caminho,'w',encoding='utf-8') as arquivo:
        json.dump(task,arquivo,indent=2)
    return