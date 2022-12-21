from django.db import models
import csv
import pandas as pd
from datetime import datetime
import os



class Arquivos_Class(models.Model):
#    def criar_extrato(caminho_arquivo_csv):
#        try:
#            with open (caminho_arquivo_csv, 'r') as arquivo:
#                arquivo_csv = csv.reader(arquivo, delimiter=';')
#        except (FileNotFoundError):
#            print('Arquivo CSV nao encontrado')
            
            
    def upload_arquivo_csv(arquivo):
        #caminho_arquivo_extrato = os.getcwd() + '\\extrato_app\\arquivos_csv\\extrato.csv'
        caminho_arquivo_extrato = os.getcwd() + '/extrato_app/arquivos_csv/extrato.csv'
        with open(caminho_arquivo, 'wb+') as destination:
            print(os.getcwd())
            for chunk in arquivo.chunks():
                destination.write(chunk)
            destination.close()

    def carregar_arquivo_csv():
        #caminho_arquivo_extrato = os.getcwd() + '\\extrato_app\\arquivos_csv\\extrato.csv'
        caminho_arquivo_extrato = os.getcwd() + '/extrato_app/arquivos_csv/extrato.csv'
        extrato = []
        descricao = []

               
        try:
            with open (caminho_arquivo_extrato, 'r', encoding='utf-8') as arquivo:
                arquivo_csv = csv.reader(arquivo, delimiter=';')
                cabecalho = csv.DictReader(arquivo, delimiter=';')

                for coluna in cabecalho:
                    print(coluna)
                    descricao.append(coluna['Descrição'])

                for i, linha in enumerate(arquivo_csv):
                    extrato.append(linha)

                arquivo.close()

                return(descricao)
        except (FileNotFoundError):
            return(False)
            