from django.db import models
import os,json
from datetime import datetime,timedelta

class Arquivos_Class(models.Model):
    # Carrega carteira
    def carrega_simulador():
        caminho_arquivo_simulador_cdb = os.getcwd() + '\\renda_fixa_app\\arquivos\\simulador_cdb.json'
        if not os.path.exists(caminho_arquivo_simulador_cdb):
            print('O arquivo ' + caminho_arquivo_simulador_cdb + 'nao existe para carregar a carteira.')
            return(False)
        else:
            with open (caminho_arquivo_simulador_cdb, 'r', encoding='utf-8') as arquivo_simulador:
                simulador_json = json.load(arquivo_simulador)
                arquivo_simulador.close()
                return(simulador_json)
            
class Manipula_data(models.Model):
    def dias_uteis(data_inicio,data_fim):
        dias_brutos = []
        data_inicio_convertida = datetime.strptime(data_inicio, '%Y-%m-%d')
        data_fim_convertida = datetime.strptime(data_fim, '%Y-%m-%d')

        dia = data_inicio_convertida
        qtd = 0
        while dia <= data_fim_convertida:
            if dia.weekday() <= 5:
                dias_brutos.append(dia.date())
                qtd = qtd + 1
            dia = dia + timedelta(days=1)
        print(qtd)

        return(dias_brutos)