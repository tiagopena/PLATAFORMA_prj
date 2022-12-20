from django.shortcuts import render
from .models import Arquivos_Class

def home(request):
    if request.POST:
        Arquivos_Class.upload_arquivo_csv(request.FILES['arquivo'])

    extrato = Arquivos_Class.carregar_arquivo_csv()

    
    
    conteudo = {
        'x' : 'x',
        'extrato' : extrato,
        }
    
    return render (request, 'home_extrato.html', context=conteudo)