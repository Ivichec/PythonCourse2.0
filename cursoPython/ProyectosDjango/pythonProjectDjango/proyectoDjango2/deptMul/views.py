from django.shortcuts import render

# Create your views here.
from deptMul.models import Formulario


def index(request):
    return render(request, "formulario/template1Index1.html")


def alta1(request):
    oper = request.POST['operacion']
    condicional = operacion(request,oper)
    context = {
        'condicional1': condicional,
        'operacion': oper
    }
    return render(request, "formulario/template1Index1.html", context)


def operacion(request, oper):
    emple = Formulario()
    if oper == 'Insertar':
        num = request.POST['dept_no']
        nom = request.POST['dnombre']
        loc = request.POST['loc']
        condicional = emple.insertdato(num, nom, loc)
    if oper == 'Modificar':
        num = request.POST['dept_no']
        loc = request.POST['loc']
        condicional = emple.modificar(num, loc)
    if oper == 'Eliminar':
        num = request.POST['dept_no']
        condicional = emple.baja(num)
    return condicional
