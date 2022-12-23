from django.shortcuts import render
from .models import Arquivos_Class
import os

def extrato_eua(request):
    caminho_arquivo_extrato = os.getcwd() + '\\extrato_app\\arquivos_csv\\extrato_eua.csv'    

    if request.POST:
        Arquivos_Class.comparar_arquivos(request.FILES['arquivo'],caminho_arquivo_extrato)

    if not os.path.exists(caminho_arquivo_extrato):
        return render (request, 'home_upload.html')
    
    if Arquivos_Class.carregar_arquivo_csv(caminho_arquivo_extrato) != False:
        conteudo_extrato = Arquivos_Class.carregar_arquivo_csv(caminho_arquivo_extrato)
        conteudo = {
            'cabecalho' : conteudo_extrato[0],
            'extrato' : conteudo_extrato[1],
            'debito' : conteudo_extrato[2],
            'saldo_debito' : conteudo_extrato[3],
            'credito' : conteudo_extrato[4],
            'saldo_credito' : conteudo_extrato[5],
            'total' : conteudo_extrato[3] + conteudo_extrato[5],
        }
        return render (request, 'home_extrato.html', context=conteudo)
    else:
        erro = 'Nao foi possivel carregar o arquivo ' + caminho_arquivo_extrato
    

    conteudo = {
        'msg_erro' : erro,
    }
    
    return render (request, 'erro.html', context=conteudo)

def relatorio_eua(request):
    caminho_arquivo_extrato = os.getcwd() + '\\extrato_app\\arquivos_csv\\extrato_eua.csv'

    if Arquivos_Class.carregar_arquivo_csv(caminho_arquivo_extrato) != False:
        conteudo_extrato = Arquivos_Class.carregar_arquivo_csv(caminho_arquivo_extrato)
        conteudo = {
            'cabecalho' : conteudo_extrato[0],
            'extrato' : conteudo_extrato[1],
            'debito' : conteudo_extrato[2],
            'saldo_debito' : conteudo_extrato[3],
            'credito' : conteudo_extrato[4],
            'saldo_credito' : conteudo_extrato[5],
            'total' : conteudo_extrato[3] + conteudo_extrato[5],
            'dividendo' : conteudo_extrato[6],
            'dividendo_imposto' : conteudo_extrato[7],
            'resto' : conteudo_extrato[8],
        }
        return render (request, 'relatorio_eua.html', context=conteudo)
    else:
        erro = 'Nao foi possivel carregar o arquivo ' + caminho_arquivo_extrato
        
    conteudo = {
        'msg_erro' : erro,
    }
    
    return render (request, 'erro.html', context=conteudo)
    