from django.contrib import admin
from django.urls import path
from cadastro_de_usuarios_no_banco import views

urlpatterns = [
    path('', views.home, name='home'),
]
