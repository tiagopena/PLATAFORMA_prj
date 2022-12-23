from django.urls import path
from extrato_app import views

app_name = 'extrato_app'


urlpatterns = [
    path('extrato_eua', views.extrato_eua, name='extrato_eua'),
    path('relatorio_eua', views.relatorio_eua, name='relatorio_eua'),    
]