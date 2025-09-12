import collector
#deleta umelemento
def delete(task):
    idd=collector.collectorID(task)
    task.pop(idd)