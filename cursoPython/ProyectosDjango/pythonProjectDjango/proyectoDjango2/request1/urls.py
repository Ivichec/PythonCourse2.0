from django.urls import path

from request1 import views

urlpatterns = [
    path('', views.index, name='index'),
    path('alta', views.empleados1 , name='empleados1'),

]