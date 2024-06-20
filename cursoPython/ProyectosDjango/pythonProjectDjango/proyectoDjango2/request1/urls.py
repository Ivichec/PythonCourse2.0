from django.urls import path

from request1 import views

urlpatterns = [
    path('', views.index, name='index'),
    path('alta', views.alta , name='Alta'),
    path('baja', views.baja , name='Baja'),
    path('modificar', views.modificar , name='Modificar'),
    path('listar', views.listar , name='Listar'),
]