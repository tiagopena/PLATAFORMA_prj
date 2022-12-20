from django.urls import path
from carteira_app import views

app_name = 'carteira_app'


urlpatterns = [
    path('', views.menu, name='menu'),
    path('registrar_compra/', views.registrar_compra, name='registrar_compra'),
    path('consultar_carteira/<str:pais>/', views.consultar_carteira, name='consultar_carteira'),    
    ]