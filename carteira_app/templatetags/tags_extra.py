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
def calcula_preco_medio(ticker,valor_compra,debito_total_compra,quantidade_compra,carteira):
    preco_medio = 0
    quantidade = float(quantidade_compra)    
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
def calcula_porcentagem(quantidade,debito_total,fechamento):
    valor_ordem = float(debito_total) / float(quantidade)
    resultado = ((float(fechamento) * 100) / float(valor_ordem)) - 100
    return(round(resultado,2))




















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
def compara_preco_medio (preco_medio,fechamento):
    if float(preco_medio) <= float(fechamento):
        return('green')
    else:
        return('red')
    
@register.simple_tag
def calcula_total_posicionado (carteira_json,pais):
    total_posicionado = 0
    total_posicionado_atualizado = 0
    for acao in carteira_json['acao']:
        if acao['pais'] == pais:
            total_posicionado = total_posicionado + float(acao['debito_total_compra'])
            total_posicionado_atualizado = total_posicionado_atualizado + (float(acao['fechamento_valor']) * float(acao['quantidade_compra']))            
    return(total_posicionado,total_posicionado_atualizado)

@register.simple_tag
def retorna_convertido (total_eua):
    hoje = datetime.now().date()

    hoje_string = datetime.strftime(hoje,format="%m-%d-%Y")
    url = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao=' + chr(39) + hoje_string + chr(39) + '&$format=json&$select=cotacaoCompra,dataHoraCotacao'
    resposta = requests.get(url)
    cotacao = resposta.json()
    codigo_retorno = resposta.status_code
    qtd = 6
    
    while codigo_retorno == 200 and cotacao['value'] == [] and qtd != 0:
        print('ENTROU NO WHILE')
        #print(hoje)
        #print(datetime.now().date())
        #print(hoje)
        #hoje_time = datetime.strptime(hoje,format="%Y-%m-%d")
        menos_um_dia = hoje - timedelta(days=1)
        menos_um_dia_string = datetime.strftime(menos_um_dia,format="%m-%d-%Y")
        url = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao=' + chr(39) + menos_um_dia_string + chr(39) + '&$format=json&$select=cotacaoCompra,dataHoraCotacao'
        resposta = requests.get(url)
        cotacao = resposta.json()
        codigo_retorno = resposta.status_code
        qtd = qtd - 1
    
    valor_cotacao = cotacao['value'][0]['cotacaoCompra']
    data_cotacao = datetime.strptime((cotacao['value'][0]['dataHoraCotacao']), '%Y-%m-%d %H:%M:%S.%f')

    total_eua_corrigido = float(total_eua) * float(valor_cotacao)
    return(valor_cotacao,data_cotacao,total_eua_corrigido)

@register.simple_tag
def totaliza_apurado(total_brasil_posicionado,total_brasil_posicionado_atualizado,total_eua_posicionado,total_eua_posicionado_atualizado,cotacao):
    total_posicionado = float(total_brasil_posicionado) + (float(total_eua_posicionado) * float(cotacao))
    total_posicionado_atualizado = float(total_brasil_posicionado_atualizado) + (float(total_eua_posicionado_atualizado) * float(cotacao))
    lucro = round((((float(total_posicionado_atualizado) * 100) / float(total_posicionado)) - 100),2)
    return(total_posicionado,total_posicionado_atualizado,lucro)
    #return(round(resultado,2))

