from django.shortcuts import render
from pandas_datareader import data as web
from .models import Arquivos_Class

def menu(request):
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
    
    conteudo = {
        'pais' : pais,
        'carteira' : Arquivos_Class.consultar_carteira(),
    }
    
    return render (request, 'consultar_carteira.html', context=conteudo)