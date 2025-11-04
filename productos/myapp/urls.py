from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # URLs para Categoría
    path('categorias/', views.CategoriaListView.as_view(), name='categoria-list'),
    path('categorias/crear/', views.CategoriaCreateView.as_view(), name='categoria-create'),
    path('categorias/<int:pk>/editar/', views.CategoriaUpdateView.as_view(), name='categoria-update'),
    path('categorias/<int:pk>/eliminar/', views.CategoriaDeleteView.as_view(), name='categoria-delete'),
    path('categorias/<int:pk>/', views.CategoriaDetailView.as_view(), name='categoria-detail'),

        # URLs para Etiqueta
    path('etiquetas/',  views.EtiquetaListView.as_view(), name='etiqueta-list'),
    path('etiquetas/crear/',  views.EtiquetaCreateView.as_view(), name='etiqueta-create'),
    path('etiquetas/<int:pk>/editar/',  views.EtiquetaUpdateView.as_view(), name='etiqueta-update'),
    path('etiquetas/<int:pk>/eliminar/',  views.EtiquetaDeleteView.as_view(), name='etiqueta-delete'),

    # URLs para Producto
    path('productos/',  views.ProductoListView.as_view(), name='producto-list'),
    path('productos/crear/',  views.ProductoCreateView.as_view(), name='producto-create'),
    path('productos/<int:pk>/editar/',  views.ProductoUpdateView.as_view(), name='producto-update'),
    path('productos/<int:pk>/eliminar/',  views.ProductoDeleteView.as_view(), name='producto-delete'),
    path('productos/<int:pk>/', views.ProductoDetailView.as_view(), name='producto-detail'),

    #Otras url
    path('productos/precio/', views.ProductoPorPrecioListView.as_view(), name='producto-por-precio'),
    path('productos/categoria/<int:categoria_id>/', views.ProductoPorCategoriaListView.as_view(), name='producto-por-categoria'),
    path('productos/excluir-sin-detalles/', views.ProductoExcluirSinDetallesListView.as_view(), name='producto-excluir-sin-detalles'),
    path('productos/anotaciones/', views.ProductoConAnotacionesListView.as_view(), name='producto-con-anotaciones'),
    path('estadisticas/', views.EstadisticasView.as_view(), name='estadisticas'),
]
