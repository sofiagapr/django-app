from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import ListView
from .models import Cliente, Transaccion

class ClienteView(ListView):
    model = Cliente
    template_name = 'listar_cliente.html'  # Nombre del template donde se mostrará la lista de clientes
    context_object_name = 'clientes'  # Nombre del contexto que contendrá la lista de clientes

    def get_queryset(self):
        return Cliente.objects.all()  # Obtener todos los clientes

class TransaccionView(ListView):
    model = Transaccion
    template_name = 'listar_transaccion.html'  # Nombre del template donde se mostrará la lista de transacciones
    context_object_name = 'transacciones'  # Nombre del contexto que contendrá la lista de transacciones

    def get_queryset(self):
        return Transaccion.objects.all()  # Obtener todas las transacciones
