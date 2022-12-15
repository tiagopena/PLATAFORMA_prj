from django import template
from pandas_datareader import data as web
from datetime import date,timedelta,datetime
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
            fechamento_ajustado = item
            print(type(item))
    elif pais == 'eua':
        for item in (web.DataReader(ticker, data_source='yahoo', start=hoje, end=hoje)['Adj Close']):
            fechamento_ajustado = item
            print(type(item))
    
    print(type(fechamento_ajustado))
    print(type(fechamento_ajustado))
    print(type(fechamento_ajustado))
    print(type(fechamento_ajustado))
    print(type(fechamento_ajustado))
    print(type(fechamento_ajustado))
    print(type(fechamento_ajustado))
    print(fechamento_ajustado)

        
    return round(float(fechamento_ajustado),2)

@register.simple_tag
def formata_data(data_eua):
    data_brasil = datetime.strptime(data_eua, '%Y-%m-%d')

    

    return(data_brasil)

#@register.simple_tag
#def formata_data(data_eua):
#    ano = data_eua.split('-')[0]
#    mes = (data_eua.split('-')[1]).split('-')[0]
#    dia = data_eua.split('-')[2]
#    data_brasil = dia + '/' + mes + '/' + ano
#
#    return(data_brasil)

#@register.simple_tag
#def converte_valor_float(valor_string):
#    valor_float = round(float(valor_string),2)    
#
#    return(valor_float)

@register.simple_tag
def calcula_porcentagem(ordem,fechamento):
    resultado = ((float(fechamento) * 100) / float(ordem)) - 100

    return(round(resultado,2))


    
