from django.shortcuts import render
from emp.models import Peliculas


def index(request):
    emple = Peliculas()
    cursor = emple.devolverdatos()
    contexto = {
        'listado_peliculas': cursor
    }
    return render(request, "template1.html", contexto)