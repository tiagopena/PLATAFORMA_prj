from django.urls import path
from renda_fixa_app import views

app_name = 'renda_fixa_app'


urlpatterns = [
    path('', views.menu, name='menu'),
    path('registrar_compra/', views.registrar_compra, name='registrar_compra'),
    path('consultar_carteira/', views.consultar_carteira, name='consultar_carteira'),
    path('simulador/<str:tipo>', views.simulador, name='simulador'),
    ]