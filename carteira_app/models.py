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

    '''

    def carrega_fechamento_ajustado():
        
        carteira_sem_fechamento =  Arquivos_Class.consultar_carteira()
        carteira_com_fechamento = []
        
        for item01 in carteira_sem_fechamento:
            #cotacao_bovespa = cotacao.DataReader(item01['codigo_b3'] + '.SA', data_source='yahoo', start = '2022-12-07', end = '2022-12-07')['Adj Close']
            
            #cotacao_bovespa = cotacao.DataReader(item01['codigo_b3'] + '.SA', data_source='yahoo', start = dt.today() - 1, end = dt.today())['Adj Close']
            for item02 in cotacao_bovespa:
                fechamento = {
                    'pais' : item01['pais'],
                    'codigo_b3' : item01['codigo_b3'],
                    'data_compra' : item01['data_compra'],
                    'quantidade_compra' : item01['quantidade_compra'],
                    'valor_compra' : item01['valor_compra'],
                    'debito_total_compra' : item01['debito_total_compra'],
                    'fechamento' : item02,
                    'stop_venda' : item01['stop_venda'],
                    'alvo_venda' : item01['alvo_venda'],
                }
                carteira_com_fechamento.append(fechamento)
                
        return(carteira_com_fechamento)
    '''


    '''







    def carrega_carteira_Class():

        with open (os.getcwd() + '/carteira_app/arquivos/carteira.json') as arquivo_json:
            carteira_json = json.load(arquivo_json)
            arquivo_json.close()

        return carteira_json





    def grava_item_carteira_Class(item_novo_json):

        json_novo = Arquivos.carrega_carteira_Class()
        
        json_novo.append(item_novo_json)
        
        with open (os.getcwd() + '/carteira_app/arquivos/carteira.json', 'w', encoding='utf-8') as arquivo_json:
            json.dump(json_novo, arquivo_json, ensure_ascii=False, indent=2)
            arquivo_json.close()

    
        

'''