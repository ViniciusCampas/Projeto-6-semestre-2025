#Feito por ViniciusH
#08/28/25
#V1.0
#Um CRUD basico que é ligado a um arquivo .json e com um sistema de busca para
#identificar palavra chaves
from os import system
import create
import read
import update
import delete
import save

#mostra no terminal o men de escolha
def menu ():
    print('\nEscolha uma opção:')
    print('1 - Adicionar Produto')
    print('2 - Listar Produtos')
    print('3 - Deletar Produto')
    print('4 - Atualizar Produto')
    print('5 - Sair')
    opcao = input('Escolha uma opção (1-5): ')
    return opcao
#caminho do arquivo .json que sera salvo
CAMINHO_ARQUIVO='Task.json'
mainTasks=save.load([],CAMINHO_ARQUIVO)
while True:
    choices=menu()
    if choices =='1':
        system('cls')
        create.createtask(mainTasks)
    elif choices =='2':
        system('cls')
        read.read(mainTasks)
    elif choices == '3':
        system('cls')
        delete.delete(mainTasks)
    elif choices == '4':
        system('cls')
        mainTasks=update.update(mainTasks)
    elif choices == '5':
        system('cls')
        break
    save.save(mainTasks,CAMINHO_ARQUIVO)