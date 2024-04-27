from django.urls import path
from .views import ClienteView, TransaccionView

urlpatterns = [
    path("listar_cliente/", ClienteView.as_view(), name="listar_cliente"),
    path("listar_transaccion/", TransaccionView.as_view(), name="listar_transaccion"),
]