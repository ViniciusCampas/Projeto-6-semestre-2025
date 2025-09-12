import datetime
#Valida se os dados coletados nao estão em branco e se a data ta noformato correto
def validatorDate (date,*values):
    for value in values:
        if not value:
            raise ValueError('Erro, por favor preencher todos osespaços')
        date_formatada = datetime.datetime.strptime(date, '%d/%m/%Y')
        dateStart=datetime.datetime.now()
        daysDif=date_formatada-dateStart
        if date_formatada<dateStart:
            return False
        return True
    return False
#Valida se o id coletados é um int
def validatorId(ids):
    if isinstance(ids, int):
        return True
    return False