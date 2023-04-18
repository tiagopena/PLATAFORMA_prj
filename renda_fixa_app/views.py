from django.shortcuts import render
from .models import Arquivos_Class,Manipula_data

def menu(request):    
    return render (request, 'menu.html')

def registrar_compra(request):
    return render (request, 'registrar_compra.html')

def consultar_carteira(request):
   json = Arquivos_Class.carrega_simulador()

   conteudo = {
         'json' : json,
      }     

   return render (request, 'consultar_carteira_renda_fixa.html', context=conteudo)

def simulador(request,tipo):
   if tipo == 'menu':
      return render (request, 'menu_simulador.html')
   elif tipo == 'cdb':
      di_anual = 13.65
      dias_uteis = 252
      capital = 5000.00
      
      json = Arquivos_Class.carrega_simulador()

      for parametro in json['parametros']:
         if parametro['modalidade'] == 'prefixada':
            parametros = parametro

      conteudo = {
         'di_anual' : di_anual,
         'dias_uteis' : dias_uteis,
         'capital' : capital,
         'json' : json,
         'parametros' : parametros,
         'dias' : Manipula_data.dias_uteis('2023-01-01','2023-12-31')
      }

      return render (request, 'simulador_cdb.html', context=conteudo)


