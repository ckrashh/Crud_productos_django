from django.contrib import admin
from .models import Categoria, Etiqueta, DetalleProducto, Producto

admin.site.register(Categoria)
admin.site.register(Etiqueta)
admin.site.register(DetalleProducto)
admin.site.register(Producto)