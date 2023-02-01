from django import template
from pandas_datareader import data as web
from datetime import date,timedelta,datetime
from django.template.defaultfilters import stringfilter
import requests
import json
from bcb import currency,PTAX

ptax = PTAX()


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
        print('======= TENTOU ACESSAR API na TAGEXTRA ===========')
        url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=' + ticker + '.SAO' + '&apikey=CX9G8JJCF9WDPS9N'
        resposta = requests.get(url)
        preco = resposta.json()
        if resposta and ('Global Quote' in preco):
            fechamento_ajustado = preco['Global Quote']['05. price']
        else:
            fechamento_ajustado = 0
            print(preco['Note'])
    elif pais == 'eua':
        print('======= TENTOU ACESSAR API na TAGEXTRA ===========')
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
def calcula_preco_medio(ticker,valor_compra,debito_total_compra,quantidade_compra,carteira):
    quantidade = float(quantidade_compra)
    preco_medio = 0
    valor_total = float(debito_total_compra)
    for acao in carteira:
        if acao['codigo_b3'] == ticker and acao['valor_compra'] != valor_compra:            
            valor_total = valor_total + float(acao['debito_total_compra'])
            quantidade = quantidade + float(acao['quantidade_compra'])
        else:
            preco_medio = float(debito_total_compra) / float(quantidade_compra)
            
    if valor_total != 0 or quantidade != 0:
        preco_medio = valor_total / quantidade

    return(preco_medio)

@register.simple_tag
def compara_preco_medio (preco_medio,fechamento):
    if float(preco_medio) <= float(fechamento):
        return('green')
    else:
        return('red')
    
@register.simple_tag
def calcula_total_posicionado (carteira_json,pais):
    total_psicionado = 0
    total_psicionado_fechado = 0
    for acao in carteira_json['acao']:
        if acao['pais'] == pais:
            total_psicionado = total_psicionado + float(acao['debito_total_compra'])
            total_psicionado_fechado = total_psicionado_fechado + (float(acao['fechamento_valor']) * float(acao['quantidade_compra']))
            
    return(total_psicionado,total_psicionado_fechado)

@register.simple_tag
def retorna_cotacao_dolar(total_eua,total_brasil):
    hoje = datetime.strftime(datetime.now(),format="%m-%d-%Y")
    url = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao=' + chr(39) + hoje + chr(39) + '&$format=json&$select=cotacaoCompra,dataHoraCotacao'
    resposta = requests.get(url)
    cotacao = resposta.json()
    valor_cotacao = cotacao['value'][1]['cotacaoCompra']
    data_cotacao = cotacao['value'][1]['dataHoraCotacao']
    total_eua_corrigido = float(total_eua) * float(valor_cotacao)
    total_eua_brasil_corrigido = total_eua_corrigido + total_brasil
    
    return(valor_cotacao,data_cotacao,total_eua_corrigido,total_eua_brasil_corrigido)