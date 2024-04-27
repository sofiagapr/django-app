from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import ListView
from .models import Cliente, Transaccion

class ClienteView(ListView):
    model = Cliente
    template_name = 'listar_cliente.html'  
    context_object_name = 'clientes'  

    def get_queryset(self):
        return Cliente.objects.all()  

class TransaccionView(ListView):
    model = Transaccion
    template_name = 'listar_transaccion.html'  
    context_object_name = 'transacciones'  

    def get_queryset(self):
        return Transaccion.objects.all()  
