from django.shortcuts import render
from pandas_datareader import data as web
from .models import Arquivos_Class
from datetime import datetime

def menu(request):
    carteira_desatualizada = Arquivos_Class.consultar_carteira()
    agora = datetime.now()

    for acao in carteira_desatualizada:
        if acao['fechamento_data'] == "" and acao['fechamento_data'] == "0":
            #Arquivos_Class.atualiza_fechamento_especifico(acao['fechamento_data'])
            print("Nunca consultado")
        elif (acao['fechamento_data'] - agora) > '0:02:01.000000':
            print('maior')
            diferenca2 = datetime.strptime(diferenca,"%Y-%m-%d %H:%M:%S")

        agora = datetime.now()
        momento = datetime.strptime("00:02:00.000000","%Y-%m-%d %H:%M:%S")

        if agora > momento:
            print('maior')
        else:
            print('menor')





    return render (request, 'menu.html')

def registrar_compra(request):
    item_novo_json = ''
    if request.POST:
        item_novo_json = {
            'pais' : request.POST['pais'],
            'codigo_b3' : request.POST['codigo_b3'].upper(),
            'data_compra' : request.POST['data_compra'],
            'quantidade_compra' : request.POST['quantidade_compra'],
            'valor_compra' : request.POST['valor_compra'],
            'debito_total_compra' : request.POST['debito_total_compra'],
            'stop_venda' : request.POST['stop_venda'],
            'alvo_venda': request.POST['alvo_venda']
    }
        print(type(item_novo_json['data_compra']))
        
        Arquivos_Class.atualiza_carteira(item_novo_json)

    return render (request, 'regitar_compra.html')

def consultar_carteira(request,pais):
    carteira = Arquivos_Class.consultar_carteira(),

    #for acao in carteira:
    #    if acao['fechamento_data'] == "" and acao['fechamento_data'] == "0":
    #        Arquivos_Class.atualiza_fechamento_especifico(acao['fechamento_data'])
    
    conteudo = {
        'pais' : pais,
        'carteira' : carteira,
    }

    #Arquivos_Class.api()
    
    return render (request, 'consultar_carteira.html', context=conteudo)