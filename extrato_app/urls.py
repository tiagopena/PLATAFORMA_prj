from django.urls import path
from extrato_app import views

app_name = 'extrato_app'


urlpatterns = [
    path('home_extrato', views.home, name='home_extrato'),
    ]