from django.shortcuts import render
from request.models import Empleado


def index(request):
    return render(request, "datos/template1.html")


def empleados(request):
    ofi = request.POST['txtOficio']
    emple = Empleado()
    cursor = emple.devolverdato(ofi)
    contexto = {
        'listado_empleados': cursor
    }
    return render(request, "datos/template2.html", contexto)

