from django.shortcuts import render
from futbol.models import Jugador


def index(request):
    emple = Jugador()
    cursor = emple.devolverdato()
    contexto = {
        'listado_empleados': cursor
    }
    return render(request, "futbol/jugadoresPrimera.html", contexto)