from django.urls import path
from ExamenDep import views

urlpatterns = [
    path('', views.index, name='index'),
    path('alta', views.alta, name='alta'),
    path('darAlta', views.darAlta, name='darAlta'),
    path('baja', views.baja, name='baja'),
    path('modificar', views.modificar, name='modificar'),
    path('editarDeptNo', views.editarDeptNo, name='editarDeptNo'),
]