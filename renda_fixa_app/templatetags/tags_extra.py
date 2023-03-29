from django import template
#from pandas_datareader import data as web
#from datetime import date,timedelta,datetime
from django.template.defaultfilters import stringfilter
#import requests
#import json
#from bcb import currency,PTAX

register = template.Library()
 
@register.simple_tag
def calcula_rentabilidade_bruta(indice,di_anual,rentabilidade_banco):
    if indice.lower() == 'cdi':
        rentabilidade_bruta = (float(di_anual)/100)*(float(rentabilidade_banco)/100)
        return(rentabilidade_bruta*100)
    else:
        return(rentabilidade_banco)

@register.simple_tag
def imposto_irpf_periodo(capital,rentabilidade_anual,dias):
    rentabilidade_mensal = (((1 + (rentabilidade_anual/100))**(1/12)) - 1) * 100
    rentabilidade_dia = (((1 + (rentabilidade_anual/100))**(1/252)) - 1) * 100
    
     

    if int(dias) <= 180:
        rendimento_sem_imposto = (capital * ((1 + (rentabilidade_mensal/100))**6)) - capital
        rendimento_com_imposto = rendimento_sem_imposto * (1 - (27.5/100))
        liquido = capital + rendimento_com_imposto
    elif int(dias) >= 181 and int(dias) <= 360:
        rendimento_sem_imposto = (capital * ((1 + (rentabilidade_mensal/100))**12)) - capital
        rendimento_com_imposto = rendimento_sem_imposto * (1 - (20/100))
        liquido = capital + rendimento_com_imposto
    elif int(dias) >= 361 and int(dias) <= 720:
        rendimento_sem_imposto = (capital * ((1 + (rentabilidade_mensal/100))**24)) - capital
        rendimento_com_imposto = rendimento_sem_imposto * (1 - (17.5/100))
        liquido = capital + rendimento_com_imposto
    elif int(dias) >= 721:
        rendimento_sem_imposto = (capital * ((1 + (rentabilidade_mensal/100))**25)) - capital
        rendimento_com_imposto = rendimento_sem_imposto * (1 - (15/100))
        liquido = capital + rendimento_com_imposto
    else:
        liquido = (capital)
    return (liquido)






@register.simple_tag
def rendimento_em_reais(capital,rentabilidade_bruta):
    total_real = float(capital) + ((float(capital) * (float(rentabilidade_bruta)/100)))
    return(total_real)


