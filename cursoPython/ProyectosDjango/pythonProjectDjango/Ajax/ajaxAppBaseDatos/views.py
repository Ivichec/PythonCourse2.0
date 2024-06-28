from django.shortcuts import render

from ajaxAppBaseDatos.models import Datos


def index(request):
    return render(request, "hospitales/Inicio.html")


def hospitales(request):
    datos = Datos()
    listahospitales = datos.hospital()
    contexto = {
        'listado_Hospitales': listahospitales
    }
    return render(request, "hospitales/Hospitales.html", contexto)


def doctores(request):
    datos = Datos()
    listadoctores = datos.doctores()
    contexto = {
        'listado_Doctores': listadoctores
    }
    return render(request, "hospitales/Doctores.html", contexto)


def plantilla(request):
    datos = Datos()
    listaplantilla = datos.plantilla()
    contexto = {
        'listado_Plantilla': listaplantilla
    }
    return render(request, "hospitales/Plantilla.html", contexto)
