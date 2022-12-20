from django.db import models
import csv
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
        caminho_arquivo = os.getcwd() + '/extrato_app/arquivos_csv/extrato.csv'
        with open(caminho_arquivo, 'wb+') as destination:
            print(os.getcwd())
            for chunk in arquivo.chunks():
                destination.write(chunk)

    def carregar_arquivo_csv():
        caminho_arquivo = os.getcwd() + '/extrato_app/arquivos_csv/extrato.csv'
        try:
            with open (caminho_arquivo, 'r') as arquivo:
                arquivo_csv = csv.reader(arquivo, delimiter=';')
                return(arquivo_csv)
        except (FileNotFoundError):
            return(False)