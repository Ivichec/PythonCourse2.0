from django.urls import path

from ajaxAppBaseDatos import views

urlpatterns = [
    path('', views.index, name='index'),
    path('viewHospitales', views.hospitales, name='Hospitales'),
    path('viewDoctores', views.doctores, name='Doctores'),
    path('viewPlantilla', views.plantilla, name='Plantilla'),
]