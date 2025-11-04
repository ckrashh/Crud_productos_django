from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from .models import Categoria, Etiqueta, DetalleProducto, Producto
from .forms import CategoriaForm, EtiquetaForm, DetalleProductoForm, ProductoForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Count, F, Sum, Value, DecimalField, ExpressionWrapper, CharField
from django.db.models.functions import Concat

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtén las categorías con más productos
        context['categorias'] = Categoria.objects.all().order_by('-id')[:4]
        # Obtén los productos más recientes
        context['productos_recientes'] = Producto.objects.all().order_by('-id')[:4]
        return context
# Vistas para Categoría
class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categoria_list.html'
    context_object_name = 'categorias'

class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria_form.html'

    def get_success_url(self):
        messages.success(self.request, 'La categoría se creó correctamente.')
        return reverse_lazy('categoria-list')

class CategoriaUpdateView(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria_form.html'

    def get_success_url(self):
        messages.info(self.request, 'La categoría se actualizó correctamente.')
        return reverse_lazy('categoria-list')

class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'categoria_confirm_delete.html'

    def get_success_url(self):
        messages.warning(self.request, 'La categoría se eliminó correctamente.')
        return reverse_lazy('categoria-list')

class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = 'categoria_detail.html'
    context_object_name = 'categoria'

# Vistas para Etiqueta
class EtiquetaListView(ListView):
    model = Etiqueta
    template_name = 'etiqueta_list.html'
    context_object_name = 'etiquetas'

class EtiquetaCreateView(CreateView):
    model = Etiqueta
    form_class = EtiquetaForm
    template_name = 'etiqueta_form.html'
    success_url = reverse_lazy('etiqueta-list')

class EtiquetaUpdateView(UpdateView):
    model = Etiqueta
    form_class = EtiquetaForm
    template_name = 'etiqueta_form.html'
    success_url = reverse_lazy('etiqueta-list')

class EtiquetaDeleteView(DeleteView):
    model = Etiqueta
    template_name = 'etiqueta_confirm_delete.html'
    success_url = reverse_lazy('etiqueta-list')

# Vistas para Producto
class ProductoListView(ListView):
    model = Producto
    template_name = 'producto_list.html'
    context_object_name = 'productos'
    paginate_by = 10  # Opcional: para paginación

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agrega las categorías para el filtro por categoría
        context['categorias'] = Categoria.objects.all()
        return context


class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto_form.html'
    success_url = reverse_lazy('producto-list')

    def form_valid(self, form):
        # Guarda el producto
        self.object = form.save(commit=False)
        self.object.save()
        form.save_m2m()

        # Crea o actualiza los detalles del producto
        dimensiones = form.cleaned_data.get('dimensiones')
        peso = form.cleaned_data.get('peso')
        if dimensiones or peso:
            detalles, created = DetalleProducto.objects.get_or_create(
                dimensiones=dimensiones,
                peso=peso
            )
            self.object.detalles = detalles
            self.object.save()
            messages.success(self.request, f'Producto "{self.object.nombre}" creado con éxito.')
        else:
            messages.success(self.request, f'Producto "{self.object.nombre}" creado con éxito (sin detalles).')

        return super().form_valid(form)

class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto_form.html'
    success_url = reverse_lazy('producto-list')

    def get_initial(self):
        initial = super().get_initial()
        if self.object.detalles:
            initial['dimensiones'] = self.object.detalles.dimensiones
            initial['peso'] = self.object.detalles.peso
        return initial

    def form_valid(self, form):
        # Actualiza el producto
        self.object = form.save(commit=False)
        self.object.save()
        form.save_m2m()

        # Actualiza los detalles del producto
        dimensiones = form.cleaned_data.get('dimensiones')
        peso = form.cleaned_data.get('peso')
        if dimensiones or peso:
            detalles, created = DetalleProducto.objects.get_or_create(
                dimensiones=dimensiones,
                peso=peso
            )
            self.object.detalles = detalles
            self.object.save()
            messages.success(self.request, f'Producto "{self.object.nombre}" actualizado con éxito.')
        else:
            messages.success(self.request, f'Producto "{self.object.nombre}" actualizado con éxito (sin detalles).')

        return super().form_valid(form)

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'producto_confirm_delete.html'
    success_url = reverse_lazy('producto-list')

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'producto_detail.html'
    context_object_name = 'producto'

# Vista para buscar productos por precio mínimo
class ProductoPorPrecioListView(ListView):
    model = Producto
    template_name = 'producto_por_precio.html'
    context_object_name = 'productos'

    def get_queryset(self):
        precio_minimo = self.request.GET.get('precio_minimo', 0)
        return Producto.objects.filter(precio__gte=precio_minimo).order_by('precio')

# Vista para buscar productos por categoría
class ProductoPorCategoriaListView(ListView):
    model = Producto
    template_name = 'producto_por_categoria.html'
    context_object_name = 'productos'

    def get_queryset(self):
        categoria_id = self.kwargs.get('categoria_id')
        return Producto.objects.filter(categoria_id=categoria_id)

# Vista para ejercicios con exclude()
class ProductoExcluirSinDetallesListView(ListView):
    model = Producto
    template_name = 'producto_excluir_sin_detalles.html'
    context_object_name = 'productos'

    def get_queryset(self):
        return Producto.objects.exclude(detalles__isnull=True)

# Vista para ejercicios con anotaciones
class ProductoConAnotacionesListView(ListView):
    model = Producto
    template_name = 'producto_con_anotaciones.html'
    context_object_name = 'productos'

    def get_queryset(self):
        return Producto.objects.annotate(
            num_etiquetas=Count('etiquetas'),
            nombre_categoria=F('categoria__nombre'),
            precio_con_iva=ExpressionWrapper(
                F('precio') * 1.16,
                output_field=DecimalField(max_digits=10, decimal_places=2)
            ),
            nombre_completo=ExpressionWrapper(
                Concat('nombre', Value(' '), 'categoria__nombre'),
                output_field=CharField()
            )
        ).order_by('precio_con_iva')

# Vista para estadísticas avanzadas
class EstadisticasView(TemplateView):
    template_name = 'estadisticas.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_productos'] = Producto.objects.count()
        context['total_categorias'] = Categoria.objects.count()
        context['precio_promedio'] = Producto.objects.aggregate(promedio=Sum('precio') / Count('id'))['promedio']
        context['categoria_con_mas_productos'] = Categoria.objects.annotate(
            num_productos=Count('productos')
        ).order_by('-num_productos').first()
        return context
