import datetime
import validator
#coleta o ID e devolve um int
def collectorID(task):
    choseId=int(input('Digite o Id da tarefa a ser alterado '))
    if validator.validatorId(choseId):
        for enum,value in enumerate(task):
            if choseId == value['Id']:
                idRefe=enum
        return idRefe
#coleta as informaçoes basicas e devolve um dicionario
def collectorDate(lenids):
    ids=1+lenids
    taskname=input('Tarefa: ')
    dateStart=datetime.datetime.now().strftime('%D/%M/%Y - %H:%M:%S')
    dateInput=input('Data de termino(DD/MM/YYYY):')
    priorit=input('Prioridade:')
    sobre=input('Sobre:')
    if validator.validatorDate(dateInput,ids,taskname,priorit,sobre):
        taskTemp={'Id':ids,'Nome':taskname,'DataInicial':dateStart,'Datafinal':dateInput,'Prioridade':priorit,'Sobre':sobre}
    return taskTemp
#coleta as informaçoes de alteração e devolve uma list
def collectorUpdate(task,idd):
    taskname=input('Tarefa: ')
    dateAlt=datetime.datetime.now().strftime('%D/%M/%Y - %H:%M:%S')
    dateInput=input('Data de termino(DD/MM/YYYY):')
    priorit=input('Prioridade:')
    sobre=input('Observacao:')
    if validator.validatorDate(dateInput,taskname,priorit,sobre):
        task[idd]['Nome']=taskname
        task[idd]['Data Inicial']=f'{task[idd]['Data Inicial']} - Datade Alteração:{dateAlt}'
        task[idd]['Data final']=dateInput
        task[idd]['Prioridade']=priorit
        task[idd]['Sobre']=sobre
    return task