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

    def comparar_arquivos (arquivo_novo):
        caminho_arquivo_novo = os.getcwd() + '\\extrato_app\\static\\merge.csv'
        caminho_arquivo_extrato = os.getcwd() + '\\extrato_app\\arquivos_csv\\extrato.csv'
        
        if os.path.exists(caminho_arquivo_extrato):
            arquivo_csv = pd.read_csv(arquivo_novo, delimiter=';')
            arquivo_extrato = pd.read_csv(caminho_arquivo_extrato, delimiter=';')

            print('PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP')
            print(type(arquivo_csv))
            print(type(arquivo_extrato))
            print('PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP')

            print('===================================')
            for linha in arquivo_csv:
                print(linha)
            print('===================================')
            for linha in arquivo_extrato:
                print(linha)
            print('===================================')
            
            
            merge = pd.merge(arquivo_csv, arquivo_extrato, how ='outer' )
            

            print(merge)

            x = merge.reindex(axis='columns')

            

            x.to_csv(caminho_arquivo_novo, index_label='Indice', sep=';')
            x.to_csv(caminho_arquivo_extrato, index_label='Indice', sep=';')
            #merge.to_csv(caminho_arquivo_novo, index=False, sep=';')
            #merge.to_csv(caminho_arquivo_extrato, index=False, sep=';')
            


            
            print('CRIOU ARQUIVO NOVO')
                
        else:
            print('CHEGOU AQUI 07')

            temporario = os.getcwd() + '\\extrato_app\\arquivos_csv\\extrato.csv'

            with open(temporario, 'wb+') as destination:
                for chunk in arquivo_novo.chunks():
                    destination.write(chunk)
                destination.close()

            x = pd.read_csv(temporario, delimiter=';')

            x.to_csv(caminho_arquivo_extrato, index_label='Indice', sep=';')



            

            '''
            with open(caminho_arquivo_extrato, 'wb+') as destination:
                for chunk in arquivo_novo.chunks():
                    destination.write(chunk)
                destination.close()
            print('nao CRIOU ARQUIVO NOVO')
            '''

        '''
        
        arquivo_csv = pd.read_csv(caminho_arquivo_novo)
        print('HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH')
        print(arquivo_csv)
        print('HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH')

        
        arquivo_novo = pd.read_csv(caminho_arquivo_extrato)
        print('HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH')
        print(arquivo_novo)
        print('HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH')

        m = pd.merge(arquivo_csv, arquivo_novo, how ='outer' )

        print('mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm')
        print(m)
        print('mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm')

        M = pd.merge(m, arquivo_csv, how ='outer' )

        print('MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM')
        print(M)
        print('MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM')

        '''


        '''

        try:
            with open (caminho_arquivo_novo, 'r', encoding='utf-8-sig') as arquivo:
                arquivo_novo_csv = csv.reader(arquivo, delimiter=';')
                for i, linha_arquivo_novo in enumerate(arquivo_novo_csv):
                    q[i] = linha_arquivo_novo
                    #set(linhas_arquivo_novo_csv).add(linha_arquivo_novo)
                    linhas_arquivo_novo_csv.append(set(linha_arquivo_novo))
                    #print(i)
                arquivo.close()
        except (FileNotFoundError):
            return(False)

        try:
            with open (caminho_arquivo_extrato, 'r', encoding='utf-8-sig') as arquivo:
                arquivo_extrato_csv = csv.reader(arquivo, delimiter=';')
                for linha_arquivo_extrato in (arquivo_extrato_csv):
                    linhas_arquivo_extrato_csv.append(set(linha_arquivo_extrato))
                    #print(i)
                arquivo.close()
        except (FileNotFoundError):
            return(False)

        print(linhas_arquivo_novo_csv)

        

    

        #print(a)

        
        x = set(linhas_arquivo_novo_csv)
        y = set(linhas_arquivo_extrato_csv)

        print(x)
        print(y)

        z = x.update(y)

        print(z)

        #for linha_novo in linhas_arquivo_novo_csv:
        #    for linha_extrato in linhas_arquivo_extrato_csv:
        #        if linha_novo == linha_extrato:
        #            linhas_arquivo_novo_csv.remove(linha_novo)
        #            print('Achou')

        #linhas_arquivo_extrato_csv.extend(linhas_arquivo_novo_csv)


        

        
            
        #print(linhas_arquivo_novo_csv)
        #print('=============================')
        #print(linhas_arquivo_extrato_csv)

        '''