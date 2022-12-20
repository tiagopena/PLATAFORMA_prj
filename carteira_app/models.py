from django.db import models
from pandas_datareader import data as cotacao
import json
import os
from datetime import date as dt


class Arquivos_Class(models.Model):
    def cria_carteira(item_json):
        with open (os.getcwd() + '/carteira_app/arquivos/carteira.json', 'w', encoding='utf-8') as arquivo_json:
            json.dump(item_json, arquivo_json, ensure_ascii=False, indent=2)
            arquivo_json.close()

    def consultar_carteira():
        try:
            with open (os.getcwd() + '/carteira_app/arquivos/carteira.json') as arquivo_json:
                carteira_json = json.load(arquivo_json)
                arquivo_json.close()
                
            return carteira_json
        except IOError:
            return("Falha de IO.")
        except FileNotFoundError:
            return("Arquivo inexistente.")

    def atualiza_carteira(item_novo_json):
        item_json = Arquivos_Class.consultar_carteira()
        item_json.append(item_novo_json)
        Arquivos_Class.cria_carteira(item_json)