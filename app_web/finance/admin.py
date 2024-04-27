from django.contrib import admin
from .models import Cliente,Producto,ClienteProducto,TipoTransaccion,Transaccion

# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('name','lastname','email','celular')


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto','abreviatura','descripcion')


class Cliente_productoAdmin(admin.ModelAdmin):
    list_display = ('cliente','producto','numero_cuenta')


class TipoTransaccionAdmin(admin.ModelAdmin):
    list_display = ('nombre','abreviatura','descripcion')

class TransaccionAdmin(admin.ModelAdmin):
    list_display = ('cliente_producto', 'monto','tipo_transaccion')

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(ClienteProducto, Cliente_productoAdmin)
admin.site.register(TipoTransaccion, TipoTransaccionAdmin)
admin.site.register(Transaccion, TransaccionAdmin)



# Register your models here.