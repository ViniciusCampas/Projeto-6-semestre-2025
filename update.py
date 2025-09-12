import collector
#faz uma alteração do elemento
def update(task):
    idd=collector.collectorID(task)
    tasks=collector.collectorUpdate(task,idd)
    return tasks