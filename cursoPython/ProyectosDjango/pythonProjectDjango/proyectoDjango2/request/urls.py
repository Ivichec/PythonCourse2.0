from django.urls import path

from request import views

urlpatterns = [
    path('', views.index, name='index'),
    path('empleados', views.empleados, name='empleados'),

]