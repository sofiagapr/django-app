import datetime
from django.db import models
from django.contrib.auth.hashers import make_password
from django.utils import timezone


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
    celular = models.CharField(max_length=20)
    contraseña= models.CharField(max_length=128, null=False, default=None)

    def save(self, *args, **kwargs):
        self.contraseña = make_password(self.contraseña)
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def _str_(self):
        return self.name


class Producto(DateTimeModel):
    nombre_producto = models.CharField(max_length=50)
    abreviatura = models.CharField(max_length=5)
    descripcion = models.CharField(max_length=100)


class ClienteProducto(DateTimeModel):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    numero_cuenta = models.CharField(max_length=20)


class TipoTransaccion(DateTimeModel):
    nombre = models.CharField(max_length=50)
    abreviatura = models.CharField(max_length=5)
    descripcion = models.CharField(max_length=200)


class Transaccion(DateTimeModel):
    cliente_producto = models.ForeignKey(ClienteProducto, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_transaccion = models.ForeignKey(TipoTransaccion, on_delete=models.CASCADE)