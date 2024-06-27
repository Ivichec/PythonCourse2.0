from django.urls import path

from Peliculas import views

urlpatterns = [
    path('', views.index, name='index'),
    path('alta', views.alta, name='Alta'),
    path('listarSerie', views.listarSerie, name='listarSerie'),
    path('insertarDato', views.insertarDato, name='insertarDato'),
    path('Borrar', views.Borrar, name='Borrar'),
    path('ResultadoBaja', views.baja1, name='baja1'),
   # path('ResultadoListar', views.listar1, name='listar1'),
]