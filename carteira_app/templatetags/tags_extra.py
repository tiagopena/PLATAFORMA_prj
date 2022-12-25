from django import template
from pandas_datareader import data as web
from datetime import date,timedelta,datetime
from django.template.defaultfilters import stringfilter
import requests
import json

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
        print('Entrou no ' + pais + ' com o ticker ' + ticker)
        url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=' + ticker + '.SAO' + '&apikey=CX9G8JJCF9WDPS9N'
        resposta = requests.get(url)
        preco = resposta.json()
        fechamento_ajustado = preco['Global Quote']['05. price']
        print(fechamento_ajustado)
        
    elif pais == 'eua':
        print('Entrou no ' + pais + ' com o ticker ' + ticker)
        url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=' + ticker + '&apikey=CX9G8JJCF9WDPS9N'
        resposta = requests.get(url)
        preco = resposta.json()
        #for item in (web.DataReader(ticker, data_source='yahoo', start=hoje, end=hoje)['Adj Close']):
        #    fechamento_ajustado = item
        #    print(type(item))
        fechamento_ajustado = preco['Global Quote']['05. price']
        print(fechamento_ajustado)
    return (float(fechamento_ajustado))

@register.simple_tag
def formata_data(data_eua):
    data_brasil = datetime.strptime(data_eua, '%Y-%m-%d')    

    return(data_brasil)

@register.simple_tag
def calcula_porcentagem(ordem,fechamento):
    resultado = ((float(fechamento) * 100) / float(ordem)) - 100

    return(round(resultado,2))