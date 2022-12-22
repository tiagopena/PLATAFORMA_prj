from django.shortcuts import render
from .models import Arquivos_Class

def home(request):
    if request.POST:
        Arquivos_Class.upload_arquivo_csv(request.FILES['arquivo'])

    cabecalho = Arquivos_Class.carregar_arquivo_csv()[0]
    extrato = Arquivos_Class.carregar_arquivo_csv()[1]

    #print(Arquivos_Class.carregar_coluna_especifica('Hora'))

    Arquivos_Class.comparar_arquivos()

    
    
    conteudo = {
        'cabecalho' : cabecalho,
        'extrato' : extrato,
        }
    
    return render (request, 'home_extrato.html', context=conteudo)