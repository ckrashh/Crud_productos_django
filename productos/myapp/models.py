from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class DetalleProducto(models.Model):
    dimensiones = models.CharField(max_length=100, blank=True, null=True)
    peso = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)


    def __str__(self):
        return f"Detalles de {self.producto.nombre}" if hasattr(self, 'producto') else "Detalles sin producto"

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    etiquetas = models.ManyToManyField(Etiqueta, related_name='productos', blank=True)
    detalles = models.OneToOneField(DetalleProducto, on_delete=models.CASCADE, related_name='producto', blank=True, null=True)

    def __str__(self):
        return self.nombre