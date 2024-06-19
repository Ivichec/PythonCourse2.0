from django.shortcuts import render
from emp.models import Empleado


def index(request):
    emple = Empleado()
    cursor = emple.devolverdatos()
    contexto = {
        'listado_empleados': cursor
    }
    return render(request, "emp/tablaEmp.html", contexto)