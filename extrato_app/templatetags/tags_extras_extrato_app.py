from django import template
from django.template.defaultfilters import stringfilter
#from django_pandas.io import read_frame
import os

register = template.Library()


@register.simple_tag
def transforma_string_float(valor_string):
    valor_float = float(valor_string)
    return(valor_float)

'''
@register.simple_tag
def mostrar_extrato():
     
    #caminho_arquivo_extrato = os.getcwd() + '/extrato_app/arquivos_csv/extrato.csv'
    caminho_arquivo_extrato = os.getcwd() + '\\extrato_app\\arquivos_csv\\extrato.csv'
    df = read_frame(caminho_arquivo_extrato)

    #x = pd.read_csv(caminho_arquivo_extrato)
    print('=======================================')
    print(caminho_arquivo_extrato)
    print(df)
    #print(pd.read_csv(caminho_arquivo_extrato))
    print('=======================================')
    

    #return(pd.read_csv(caminho_arquivo_extrato))
    return(df)
'''