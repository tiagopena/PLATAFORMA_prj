from django import template
#from pandas_datareader import data as web
#from datetime import date,timedelta,datetime
from django.template.defaultfilters import stringfilter
#import requests
#import json
#from bcb import currency,PTAX

register = template.Library()

@register.simple_tag
def calcula_rentabilidade_cdb_imposto(indice,taxa,meses,rentabilidade_banco):
    if indice.lower() == 'cdi':
        taxa_mensal = (((1 + (float(taxa)/100)) ** (1/12)) - 1) * 100
        rentabilidade_real_mesal = taxa_mensal * (rentabilidade_banco/100)
        taxa_real_sem_imposto = (1 + (rentabilidade_real_mesal/100)) ** int(meses)
        if int(meses) <= 6:
            rentabilidade_com_imposto = taxa_real_sem_imposto * (1 - 0.275)
        elif int(meses) <= 12:
            rentabilidade_com_imposto = taxa_real_sem_imposto * (1 - 0.20)
        elif int(meses) <= 24:
            rentabilidade_com_imposto = taxa_real_sem_imposto * (1 - 0.175)
        elif int(meses) <= 25:
            rentabilidade_com_imposto = taxa_real_sem_imposto * (1 - 0.15)
        return(rentabilidade_com_imposto)
    else:
        return(rentabilidade_banco)
 
@register.simple_tag
def calcula_rentabilidade_bruta(indice,di_anual,rentabilidade_banco):
    if indice.lower() == 'cdi':
        rentabilidade_bruta = (float(di_anual)/100)*(float(rentabilidade_banco)/100)
        return(rentabilidade_bruta*100)
    else:
        return(rentabilidade_banco)

@register.simple_tag
def imposto_irpf_periodo(capital,rentabilidade_anual,mes):
    #rentabilidade_anual = 13.65


    rentabilidade_mensal = (((1 + (rentabilidade_anual/100))**(1/12)) - 1) * 100
    rentabilidade_dia = (((1 + (rentabilidade_anual/100))**(1/252)) - 1) * 100

    rendimento_sem_imposto = (capital * ((1 + (rentabilidade_mensal/100))**(    ))) - capital

    print('===========================')
    print('Rentabilidade dia: {0}'.format(rentabilidade_dia))
    print('Rentabilidade mes: {0}'.format(rentabilidade_mensal))
    print('Rentabilidade sem imposto: {0}'.format(rendimento_sem_imposto))
    print('===========================')
    
     

    if int(mes) <= 6:
        rendimento_com_imposto = rendimento_sem_imposto * (1 - (27.5/100))
        liquido = capital + rendimento_com_imposto
    elif int(mes) > 6 and int(mes) <= 12:
        rendimento_com_imposto = rendimento_sem_imposto * (1 - (20/100))
        liquido = capital + rendimento_com_imposto
    elif int(mes) > 12 and int(mes) <= 24:
        rendimento_com_imposto = rendimento_sem_imposto * (1 - (17.5/100))
        liquido = capital + rendimento_com_imposto
    elif int(mes) > 24:
        rendimento_com_imposto = rendimento_sem_imposto * (1 - (15/100))
        liquido = capital + rendimento_com_imposto
    else:
        rendimento_sem_imposto = capital
        rendimento_com_imposto = capital
        liquido = capital
    return (rendimento_sem_imposto,rendimento_com_imposto,liquido)






@register.simple_tag
def rendimento_em_reais(capital,rentabilidade_bruta):
    total_real = float(capital) + ((float(capital) * (float(rentabilidade_bruta)/100)))
    return(total_real)


