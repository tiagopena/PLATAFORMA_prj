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
        with open(caminho_arquivo_extrato, 'wb+') as destination:
            for chunk in arquivo.chunks():
                destination.write(chunk)
            destination.close()

    def carregar_arquivo_csv():
        #caminho_arquivo_extrato = os.getcwd() + '\\extrato_app\\arquivos_csv\\extrato.csv'
        caminho_arquivo_extrato = os.getcwd() + '/extrato_app/arquivos_csv/extrato.csv'
        extrato = []
        cabecalho = []
               
        try:
            with open (caminho_arquivo_extrato, 'r', encoding='utf-8-sig') as arquivo:
                arquivo_csv = csv.reader(arquivo, delimiter=';')
                tabela = csv.DictReader(arquivo, delimiter=';')

                for i, linha in enumerate(arquivo_csv):
                    if i == 0:
                        cabecalho.append(linha)
                    else:
                        extrato.append(linha)
                        
                arquivo.close()
                
                return(cabecalho,extrato)

        except (FileNotFoundError):
            return(False)

    def carregar_coluna_especifica(nome_coluna):
        #caminho_arquivo_extrato = os.getcwd() + '\\extrato_app\\arquivos_csv\\extrato.csv'
        caminho_arquivo_extrato = os.getcwd() + '/extrato_app/arquivos_csv/extrato.csv'
        conteudo_coluna = []

        try:
            with open (caminho_arquivo_extrato, 'r', encoding='utf-8-sig') as arquivo:
                tabela = csv.DictReader(arquivo, delimiter=';')

                for coluna in tabela:
                    conteudo_coluna.append(coluna[nome_coluna])

                arquivo.close()
                
                return(conteudo_coluna)

        except (FileNotFoundError):
            return(False)