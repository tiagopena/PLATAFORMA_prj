from django.shortcuts import render
from pandas_datareader import data as web
from .models2 import Arquivos_Class
from datetime import datetime,timedelta

def menu(request):
    if Arquivos_Class.carteira_atualizada == False:
        mensagem_erro = 'Arquivo com a carteira não existe'
        conteudo = {
            'mensagem_erro' : mensagem_erro
        }
        return render (request, 'erro_carteira.html', context=conteudo)
    else:
        return render (request, 'menu.html')

def consultar_carteira(request,pais):
    if Arquivos_Class.carteira_atualizada == False:
        mensagem_erro = 'Arquivo com a carteira não existe'
        conteudo = {
            'mensagem_erro' : mensagem_erro
        }
        return render (request, 'erro_carteira.html', context=conteudo)
    else:
        conteudo = {
            'pais' : pais,
            'carteira' : Arquivos_Class.carteira_atualizada(),
        }
        return render (request, 'consultar_carteira.html', context=conteudo)

def ordenar_carteira(request,pais,chave,ordem):
    if Arquivos_Class.carteira_atualizada == False:
        mensagem_erro = 'Arquivo com a carteira não existe'
        conteudo = {
            'mensagem_erro' : mensagem_erro
        }
        return render (request, 'erro_carteira.html', context=conteudo)
    else:
        carteira_acao = Arquivos_Class.carteira_atualizada()['acao']
        carteira_acao.sort(key=lambda x: x[chave],reverse=False)
        carteira_ordenada = {
            "ultima_consulta":Arquivos_Class.carteira_atualizada()['ultima_consulta'],
            "acao": carteira_acao
        }

        conteudo = {
            'pais' : pais,
            'carteira' : carteira_ordenada,
        }
        return render (request, 'consultar_carteira.html', context=conteudo)


def registrar_compra(request):
    item_novo_json = ''
    if request.POST:
        consulta_api = Arquivos_Class.consulta_api(request.POST['pais'],request.POST['codigo_b3'])
        if consulta_api != False:
            item_novo_json = {
                'pais' : request.POST['pais'],
                'codigo_b3' : request.POST['codigo_b3'].upper(),
                'data_compra' : request.POST['data_compra'],
                'quantidade_compra' : request.POST['quantidade_compra'],
                'valor_compra' : request.POST['valor_compra'],
                'debito_total_compra' : request.POST['debito_total_compra'],
                'stop_venda' : request.POST['stop_venda'],
                'alvo_venda': request.POST['alvo_venda'],
                "fechamento_data": consulta_api[1],
                "fechamento_valor": consulta_api[0]
            }
            Arquivos_Class.atualizar_carteira(item_novo_json)
        else:
            print('Nao foi possivel consultar a API.')

    return render (request, 'regitar_compra.html')