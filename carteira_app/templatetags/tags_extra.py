from django import template
from pandas_datareader import data as web
from datetime import date,timedelta
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.simple_tag
def fechamento(ticker,pais):
    hoje = date.today()
    dia_semana = date.weekday(date.today())
    fechamento_ajustado = ''
    
    while dia_semana >= 5:
        dia_semana = dia_semana - 1
        hoje =  hoje + timedelta(days=-1)

    if pais == 'brasil':
        for item in (web.DataReader(ticker + '.SA', data_source='yahoo', start=hoje, end=hoje)['Adj Close']):
            fechamento_ajustado = round(item,2)
    elif pais == 'eua':
        for item in (web.DataReader(ticker, data_source='yahoo', start=hoje, end=hoje)['Adj Close']):
            fechamento_ajustado = round(item,2)

    print(fechamento_ajustado,type(fechamento_ajustado))
    
        
    return(fechamento_ajustado)

@register.simple_tag
def formata_data(data_eua):
    ano = data_eua.split('-')[0]
    mes = (data_eua.split('-')[1]).split('-')[0]
    dia = data_eua.split('-')[2]
    data_brasil = dia + '/' + mes + '/' + ano

    return(data_brasil)

@register.simple_tag
def converte_valor_float(valor_string):
    valor_float = float(valor_string)

    print(valor_float,type(valor_float))

    return(valor_float)


    
