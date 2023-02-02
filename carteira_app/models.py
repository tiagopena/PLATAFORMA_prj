from django.db import models
#from pandas_datareader import data as cotacao
import json
import os
from datetime import datetime,timedelta
import requests
import tempfile
import shutil
import yfinance as yf


class Arquivos_Class(models.Model):
    # Carrega carteira
    def carrega_carteira():
        caminho_arquivo_carteira = os.getcwd() + '\\carteira_app\\arquivos\\carteira.json'
        if not os.path.exists(caminho_arquivo_carteira):
            print('O arquivo ' + caminho_arquivo_carteira + 'nao existe para carregar a carteira.')
            return(False)
        else:
            with open (caminho_arquivo_carteira, 'r', encoding='utf-8') as arquivo_carteira:
                carteira_json = json.load(arquivo_carteira)
                arquivo_carteira.close()
                return(carteira_json)

    # Atualizar carteira com novo fechamento
    def atualizar_fechamento_carteira():
        caminho_arquivo_carteira = os.getcwd() + '\\carteira_app\\arquivos\\carteira.json'
        if not os.path.exists(caminho_arquivo_carteira):
            print('O arquivo ' + caminho_arquivo_carteira + 'nao existe para atualizar a carteira.')
            return(False)
        else:
            with open (caminho_arquivo_carteira, 'r', encoding='utf-8') as arquivo_carteira, \
                tempfile.NamedTemporaryFile('w', delete=False) as arquivo_temporario:
                carteira_json = json.load(arquivo_carteira)
                ultima_consulta = datetime.strptime(carteira_json['ultima_consulta'],"%Y-%m-%d %H:%M:%S")
                for acao in carteira_json['acao']:
                    resultado = Arquivos_Class.consulta_api_yfinance(acao['pais'],acao['codigo_b3'])
                    #acao['fechamento_data'] = '2023-02-02'
                    acao['fechamento_valor'] = resultado
                carteira_json['ultima_consulta'] = datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S")
                json.dump(carteira_json,arquivo_temporario,ensure_ascii=False,indent=4,separators=(',',':'))
            shutil.move(arquivo_temporario.name, caminho_arquivo_carteira)
            arquivo_carteira.close()
            arquivo_temporario.close()
            return(carteira_json)

    def consulta_api_yfinance(pais,ticker):
        # https://pypi.org/project/yfinance/
        if pais == 'brasil':
            #url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=' + ticker + '.SAO&apikey=CX9G8JJCF9WDPS9N'
            resposta_ticker = yf.Ticker(ticker + ".SA")
        elif pais == 'eua':
            #url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=' + ticker + '&apikey=CX9G8JJCF9WDPS9N'
            resposta_ticker = yf.Ticker(ticker)
        open = (resposta_ticker.history(period="1d")).iat[0,0]
        high = (resposta_ticker.history(period="1d")).iat[0,1]
        low = (resposta_ticker.history(period="1d")).iat[0,2]
        close = (resposta_ticker.history(period="1d")).iat[0,3]
        volume = (resposta_ticker.history(period="1d")).iat[0,4]
        dividends = (resposta_ticker.history(period="1d")).iat[0,5]
        stock_splits = (resposta_ticker.history(period="1d")).iat[0,6]
        print(resposta_ticker.history(period="1d"))
        return(float(close))

    def adiciona_item_carteira(item_novo_json):
        caminho_arquivo = os.getcwd() + '/carteira_app/arquivos/carteira.json'

        # Se o arquivo nao existe, sera criado:
        if not os.path.exists(caminho_arquivo):
            json_inicial = {
                "ultima_consulta": datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S"),
                "acao" : [item_novo_json]
            }
            with open (caminho_arquivo, 'w', encoding='utf-8') as arquivo_json:
                json.dump(json_inicial, arquivo_json, ensure_ascii=False, indent=2)
                arquivo_json.close()
        else:
            with open (caminho_arquivo, 'r', encoding='utf-8') as arquivo_carteira, \
                tempfile.NamedTemporaryFile('w', delete=False) as arquivo_temporario:
                carteira_desatualizada_json = json.load(arquivo_carteira)
                carteira_desatualizada_json['acao'].append(item_novo_json)
                carteira_desatualizada_json['ultima_consulta'] = datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S")
                json.dump(carteira_desatualizada_json,arquivo_temporario,ensure_ascii=False,indent=4,separators=(',',':'))
            shutil.move(arquivo_temporario.name, caminho_arquivo)
            arquivo_carteira.close()
            arquivo_temporario.close()





        


















    '''


    # Consulta carteira
    def consulta_carteira():
        caminho_arquivo_carteira = os.getcwd() + '\\carteira_app\\arquivos\\carteira.json'
        if not os.path.exists(caminho_arquivo_carteira):
            return(False)
        #else:
        #    with open (caminho_arquivo_carteira, 'r', encoding='utf-8')


    # Registrar itens


    # Atualizar itens
    def carteira_atualizada():
        agora = datetime.now()
        dois_dias = timedelta(hours=48.1)
        um_minuto = timedelta(seconds=61)
        qtd_api = 0
        caminho_arquivo_carteira = os.getcwd() + '\\carteira_app\\arquivos\\carteira.json'
        if os.path.exists(caminho_arquivo_carteira):
            with open (caminho_arquivo_carteira, 'r', encoding='utf-8') as arquivo_carteira, \
                tempfile.NamedTemporaryFile('w', delete=False) as arquivo_temporario:
                carteira_json = json.load(arquivo_carteira)
                ultima_consulta = datetime.strptime(carteira_json['ultima_consulta'],"%Y-%m-%d %H:%M:%S")
                if (agora - ultima_consulta) > um_minuto:
                    for acao in carteira_json['acao']:
                        data_fechamento = datetime.strptime(acao['fechamento_data'],"%Y-%m-%d")                    
                        if ((agora - data_fechamento) > dois_dias) and (qtd_api < 5):
                            resultado = Arquivos_Class.consulta_api(acao['pais'],acao['codigo_b3'])
                            #print(type(resultado[1]))
                            acao['fechamento_data'] = resultado[1]
                            acao['fechamento_valor'] = resultado[0]
                            qtd_api = qtd_api + 1
                        else:
                            print('{0} foi atualizado a menos de dois dias'.format(acao['codigo_b3']))
                    carteira_json['ultima_consulta'] = datetime.strftime(agora,"%Y-%m-%d %H:%M:%S")
                else:
                    print('A ultima consulta foi realizada em {0}'.format(ultima_consulta))
                json.dump(carteira_json,arquivo_temporario,ensure_ascii=False,indent=4,separators=(',',':'))
            shutil.move(arquivo_temporario.name, caminho_arquivo_carteira)
            arquivo_carteira.close()
            arquivo_temporario.close()
            return(carteira_json)
        else:
            print('O arquivo {0} nao existe.',format(caminho_arquivo_carteira))
            return(False)








    




    
    





    

    def consulta_api(pais,ticker):
        if pais == 'brasil':
            print('======= TENTOU ACESSAR API no MODELS ===========')
            url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=' + ticker + '.SAO&apikey=CX9G8JJCF9WDPS9N'
        elif pais == 'eua':
            print('======= TENTOU ACESSAR API no MODELS ===========')
            url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=' + ticker + '&apikey=CX9G8JJCF9WDPS9N'            
        resposta = requests.get(url)
        json_acao = resposta.json()

        if 'Global Quote' not in json_acao:
            return(False)
        else:
            print(json_acao)
            return(json_acao['Global Quote']['05. price'],json_acao['Global Quote']['07. latest trading day'])

    
    

    

    def consutar_carteira():
        caminho_arquivo = os.getcwd() + '/carteira_app/arquivos/carteira.json'
        if os.path.exists(caminho_arquivo):
            with open (caminho_arquivo) as arquivo_json:
                carteira_existente_json = json.load(arquivo_json)
                arquivo_json.close()
            return(carteira_existente_json)
        else:
            return(False)

    

    def atualiza_fechamento(posicao,nova_data,novo_valor):
        json_antigo = Arquivos_Class.consutar_carteira()

        for item in json_antigo:
            if json_antigo.index(item) == posicao:













'''

























    





    '''
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
        #item_json = Arquivos_Class.consultar_carteira()
        #item_json.append(item_novo_json)
        #Arquivos_Class.cria_carteira(item_json)

    def api ():
        
        url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=PETR4.SAO&apikey=CX9G8JJCF9WDPS9N'
        resposta = requests.get(url)
        preco = resposta.json()


        print('=================================================')





        print(preco['Global Quote']['05. price'])
        print('=================================================')

    
    '''