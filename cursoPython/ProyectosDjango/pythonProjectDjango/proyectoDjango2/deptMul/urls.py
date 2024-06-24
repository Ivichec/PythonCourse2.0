from django.urls import path

from deptMul import views

urlpatterns = [
    path('', views.index, name='index'),
    path('formulario', views.alta1, name='formulario'),
]