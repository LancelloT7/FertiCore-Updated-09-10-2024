from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_pedidos/', views.cadPedidos, name ='cadPedidos'),
    path('listar_pedidos/', views.listar_pedidos, name='listar_pedidos'),
    
]