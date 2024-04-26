import datetime
from django.db import models


class DateTimeModel(models.Model):
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(default=datetime.datetime.now())
    deleted_at = models.DateTimeField(null=True, blank=True)

    # Condición que nos indica que el modelo no es visible
    class Meta:
        abstract = True


class Cliente(DateTimeModel):
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True)
    celular = models.CharField()


class Producto(DateTimeModel):
    nombre_producto = models.CharField(max_length=50)
    abreviatura = models.CharField(max_length=5)
    descripcion = models.CharField(max_length=100)


class ClienteProducto(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    numero_cuenta = models.CharField(max_length=20)


class TipoTransaccion(models.Model):
    nombre = models.CharField(max_length=50)
    abreviatura = models.CharField(max_length=5)
    descripcion = models.CharField(max_length=200)


class Transaccion(models.Model):
    cliente_producto = models.ForeignKey(ClienteProducto, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_transaccion = models.ForeignKey(TipoTransaccion, on_delete=models.CASCADE)