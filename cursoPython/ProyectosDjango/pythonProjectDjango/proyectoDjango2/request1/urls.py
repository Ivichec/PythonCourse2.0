from django.urls import path

from request1 import views

urlpatterns = [
    path('', views.index, name='index'),
    path('alta', views.alta, name='Alta'),
    path('baja', views.baja, name='Baja'),
    path('modificar', views.modificar, name='Modificar'),
    path('listar', views.listar1, name='Listar'),
    path('ResultadoAlta', views.alta1, name='alta1'),
    path('ResultadoBaja', views.baja1, name='baja1'),
    path('ResultadoModificar', views.modificar1, name='modificar1'),
   # path('ResultadoListar', views.listar1, name='listar1'),
]