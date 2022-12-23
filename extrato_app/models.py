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
            
            
    #def upload_arquivo_csv(arquivo):
    #    #caminho_arquivo_extrato = os.getcwd() + '\\extrato_app\\arquivos_csv\\extrato.csv'
    #    caminho_arquivo_extrato = os.getcwd() + '/extrato_app/arquivos_csv/extrato.csv'
    #    with open(caminho_arquivo_extrato, 'wb+') as destination:
    #        for chunk in arquivo.chunks():
    #            destination.write(chunk)
    #        destination.close()

    
    def carregar_arquivo_csv(caminho_arquivo_extrato):
        extrato = []
        cabecalho = []
        debito = []
        credito = []        
        saldo_debito = 0
        saldo_credito = 0
        dividendo = []
        saldo_dividendo = 0
        dividendo_imposto = []
        Saldo_dividendo_imposto = 0
        compra = []
        saldo_compra = 0
        venda = []
        saldo_venda = 0
        cambio = []
        saldo_cambio = 0
        taxa = []
        saldo_taxa = 0
        resto = []
        saldo_resto = 0        
        
        try:
            with open (caminho_arquivo_extrato, 'r', encoding='utf-8-sig') as arquivo:
                arquivo_csv = csv.reader(arquivo, delimiter=';')
                for i, linha in enumerate(arquivo_csv):
                    if i == 0:
                        cabecalho.append(linha)
                    else:
                        extrato.append(linha) # Cria o extrato completo
                        if float(linha[4]) < 0: # Cria debito e ccredito
                            debito.append(linha) # Cria apenas o debito
                            saldo_debito = saldo_debito + float(linha[4]) # Faz a soma
                        else:
                            credito.append(linha) # Cria apenas o credito
                            saldo_credito = saldo_credito + float(linha[4]) # Faz a soma
                        if (('Dividendo' or 'dividendo') in linha[3]) and (not ('Imposto' or 'imposto') in linha[3]):
                            dividendo.append(linha)
                            saldo_dividendo = saldo_dividendo + float(linha[4])
                        elif (('Dividendo' or 'dividendo') in linha[3]) and (('Imposto' or 'imposto') in linha[3]):
                            dividendo_imposto.append(linha)
                            Saldo_dividendo_imposto = Saldo_dividendo_imposto + float(linha[4])
                        elif (('Compra' or 'compra') in linha[3]):
                            compra.append(linha)
                            saldo_compra = saldo_compra + float(linha[4])
                        elif (('Venda' or 'venda') in linha[3]):
                            venda.append(linha)
                            saldo_venda = saldo_venda + float(linha[4])
                        elif 'mbio' in linha[3]:
                            cambio.append(linha)
                            saldo_cambio = saldo_cambio + float(linha[4])
                        elif ('Taxa' or 'taxa') in linha[3]:
                            taxa.append(linha)
                            saldo_taxa = saldo_taxa + float(linha[4])
                        else:
                            resto.append(linha)
                            saldo_resto = saldo_resto + float(linha[4])
                            
                arquivo.close()
                return(
                    cabecalho,
                    extrato,
                    debito,
                    saldo_debito,
                    credito,
                    saldo_credito,
                    dividendo,
                    saldo_dividendo,
                    dividendo_imposto,
                    Saldo_dividendo_imposto,
                    compra,
                    saldo_compra,
                    venda,
                    saldo_venda,
                    cambio,
                    saldo_cambio,
                    taxa,
                    saldo_taxa,
                    resto,
                    saldo_resto
                )
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

    def comparar_arquivos (arquivo_novo,caminho_arquivo_extrato):
        
        if os.path.exists(caminho_arquivo_extrato):
            data_frame_novo = pd.read_csv(arquivo_novo, delimiter=';')
            data_frame_novo['Data'] = pd.to_datetime(data_frame_novo['Data'], dayfirst=True)

            data_frame_extrato = pd.read_csv(caminho_arquivo_extrato, delimiter=';')
            data_frame_extrato['Data'] = pd.to_datetime(data_frame_extrato['Data'], dayfirst=True)

            merge = pd.merge(data_frame_novo, data_frame_extrato, how ='outer' )
            merge.sort_values(by=['Data','Hora'], ascending=True, inplace=True)
            merge.to_csv(caminho_arquivo_extrato, index=False, sep=';')
            
        else:
            temporario = os.getcwd() + '\\extrato_app\\arquivos_csv\\temporario.csv'
            with open(temporario, 'wb+') as destination:
                for chunk in arquivo_novo.chunks():
                    destination.write(chunk)
                destination.close()
            data_frame_temporario_extrato = pd.read_csv(temporario, delimiter=';')
            data_frame_temporario_extrato['Data'] = pd.to_datetime(data_frame_temporario_extrato['Data'], dayfirst=True)            
            data_frame_temporario_extrato.sort_values(by=['Data','Hora'], ascending=True, inplace=True)
            
            data_frame_temporario_extrato.to_csv(caminho_arquivo_extrato, index=False, sep=';')



            

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