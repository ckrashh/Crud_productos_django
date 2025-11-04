from django import forms
from .models import Categoria, Etiqueta, DetalleProducto, Producto
from django.core.exceptions import ValidationError

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']

class EtiquetaForm(forms.ModelForm):
    class Meta:
        model = Etiqueta
        fields = ['nombre']

class DetalleProductoForm(forms.ModelForm):
    class Meta:
        model = DetalleProducto
        fields = ['dimensiones', 'peso']

class ProductoForm(forms.ModelForm):
    dimensiones = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: 10x20x30 cm'
        })
    )
    peso = forms.DecimalField(
        max_digits=6,
        decimal_places=2,
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: 1.5'
        })
    )

    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'categoria', 'etiquetas']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Configura los widgets y mensajes de error
        self.fields['nombre'].widget.attrs.update({'class': 'form-control'})
        self.fields['nombre'].error_messages = {
            'required': 'El nombre del producto es obligatorio.',
        }

        self.fields['descripcion'].widget.attrs.update({'class': 'form-control', 'rows': 3})
        self.fields['descripcion'].required = False  # Opcional

        self.fields['precio'].widget.attrs.update({'class': 'form-control'})
        self.fields['precio'].error_messages = {
            'required': 'El precio es obligatorio.',
            'invalid': 'Ingresa un precio válido (ej: 19.99).',
        }

        self.fields['categoria'].widget.attrs.update({'class': 'form-select'})
        self.fields['categoria'].error_messages = {
            'required': 'La categoría es obligatoria.',
        }

        self.fields['etiquetas'].widget = forms.CheckboxSelectMultiple()
        self.fields['etiquetas'].required = False  # Las etiquetas son opcionales
        self.fields['etiquetas'].widget.attrs.update({'class': 'form-check-input'})
        # Opcional: Queryset para las etiquetas (si necesitas filtrar)
        self.fields['etiquetas'].queryset = Etiqueta.objects.all()

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio and precio <= 0:
            raise ValidationError('El precio debe ser mayor que cero.')
        return precio