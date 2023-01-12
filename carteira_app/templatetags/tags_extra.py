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
        url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=' + ticker + '.SAO' + '&apikey=CX9G8JJCF9WDPS9N'
        resposta = requests.get(url)
        preco = resposta.json()
        if resposta and ('Global Quote' in preco):
            fechamento_ajustado = preco['Global Quote']['05. price']
        else:
            fechamento_ajustado = 0
            print(preco['Note'])
    elif pais == 'eua':
        print('Entrou no ' + pais + ' com o ticker ' + ticker)
        url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=' + ticker + '&apikey=CX9G8JJCF9WDPS9N'
        resposta = requests.get(url)
        preco = resposta.json()
        if resposta and ('Global Quote' in preco):
            fechamento_ajustado = preco['Global Quote']['05. price']
        else:
            fechamento_ajustado = 0
            print(preco['Note'])

    return (float(fechamento_ajustado))

@register.simple_tag
def formata_data(data_eua):
    data_brasil = datetime.strptime(data_eua, '%Y-%m-%d')    

    return(data_brasil)

@register.simple_tag
def calcula_porcentagem(ordem,fechamento):
    resultado = ((float(fechamento) * 100) / float(ordem)) - 100

    return(round(resultado,2))

@register.simple_tag
def calcula_preco_medio(ticker,valor_compra,carteira):
    quantidade = 0
    preco_medio = 0
    valor_total = 0
    for acao in carteira['acao']:
        if acao['codigo_b3'] == ticker and acao['valor_compra'] != valor_compra:
            quantidade = quantidade + acao['quantidade_compra']
            valor_total = valor_total + (acao['valor_compra'] * acao['quantidade_compra'])