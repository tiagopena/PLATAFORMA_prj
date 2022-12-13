from django.shortcuts import render
from pandas_datareader import data as web
from .models import Arquivos_Class

def menu(request):
    return render (request, 'menu.html')


def registrar_compra(request):

    item_novo_json = ''

    print(request.POST)

    if request.POST:
        item_novo_json = {
            'pais' : request.POST['pais'],
            'codigo_b3' : request.POST['codigo_b3'],
            'data_compra' : request.POST['data_compra'],
            'quantidade_compra' : request.POST['quantidade_compra'],
            'valor_compra' : request.POST['valor_compra'],
            'debito_total_compra' : request.POST['debito_total_compra'],
            'stop_venda' : request.POST['stop_venda'],
            'alvo_venda': request.POST['alvo_venda']
        }
        
        Arquivos_Class.atualiza_carteira(item_novo_json)

    return render (request, 'regitar_compra.html')

def consultar_carteira(request,pais):
    
    conteudo = {
        'pais' : pais,
        'carteira' : Arquivos_Class.consultar_carteira(),
        'fechamento' : Arquivos_Class.carrega_fechamento_ajustado()
    }
    
    return render (request, 'consultar_carteira.html', context=conteudo)






'''

def registrar_compra2(request):

    alias = []

    carteira_json = Arquivos_Class.consultar_carteira()

    for item in carteira_json:
        df = web.DataReader(item['codigo_b3'], data_source='yahoo', start=f'02-20-2020', end='02-20-2021')
        alias.append(item['alias'])
        print('==================================')
        print(df)
        print('==================================')    

    context = {
        'alias' : alias
    }

    return render (request, 'regitar_compra.html', context=context)
'''