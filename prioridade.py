import spacy#python -m spacy download pt_core_news_sm

nlp = spacy.load('pt_core_news_sm')

def classificarPrioridade(texto):

    doc = nlp(texto.lower())

    prioridade = 0

    palavras_urgencia = ['urgente', 'imediato', 'emergência', 'agora', 'crítico', 'pressa', 'rápido', 'já']
    palavras_importancia = ['importante', 'prioridade', 'essencial', 'crucial', 'revisar', 'atenção', 'garantir', 'retorno', 'última']
    palavras_curto_prazo = ['hoje', 'amanhã', 'logo', 'antes', 'semana', 'mês', 'final', 'breve', 'agora']

    for token in doc:
        if token.text in palavras_urgencia:
            prioridade += 3
        elif token.text in palavras_importancia:
            prioridade += 2
        elif token.text in palavras_curto_prazo:
            prioridade += 1

    return prioridade
