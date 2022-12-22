from django.shortcuts import render
from .models import Arquivos_Class
import os

def home(request):
    caminho_arquivo_extrato = os.getcwd() + '\\extrato_app\\arquivos_csv\\extrato.csv'

    

    if request.POST:
        Arquivos_Class.comparar_arquivos(request.FILES['arquivo'])

    if not os.path.exists(caminho_arquivo_extrato):
        return render (request, 'home_upload.html')

    

        

    cabecalho = Arquivos_Class.carregar_arquivo_csv()[0]
    extrato = Arquivos_Class.carregar_arquivo_csv()[1]
    

    #print(Arquivos_Class.carregar_coluna_especifica('Hora'))

    #Arquivos_Class.comparar_arquivos()

    
    
    conteudo = {
        'cabecalho' : cabecalho,
        'extrato' : extrato,
        }
    
    return render (request, 'home_extrato.html', context=conteudo)