from django.shortcuts import render
from Peliculas.models import Empleado1


def index(request):
    emple = Empleado1()
    condicional = emple.devolverdato()
    condicional1 = {
        'datos': condicional,
        'home': True,
        'personajes': False
    }
    return render(request, "data/template1Index.html",condicional1)
def listarSerie(request):
    ser = request.GET['Serie']
    emple = Empleado1()
    condicional = emple.devolverserie(ser)
    condicional1 = {
        'datos': condicional,
        'home': False,
        'personajes': True
    }
    return render(request, "data/template1Index.html", condicional1)

def alta(request):

    return render(request, "data/template2Alta.html")


def baja(request):
    return render(request, "data/template3Baja.html")


def modificar(request):
    return render(request, "data/template4Modificar.html")


def listar(request):
    return render(request, "data/template5Listado.html")


def alta1(request):
    idper = request.POST['idper']
    nombre = request.POST['nom']
    img = request.POST['img']
    idserie = request.POST['idserie']
    emple = Empleado1()
    condicional = emple.insertdato(idper, nombre, img, idserie)
    condicional1 = {
        'condicional1': condicional,
        'crud': 'ALTA'
    }
    return render(request, "data/template1Index.html", condicional1)


def baja1(request):
    dept = request.POST['dept_no']
    emple = Empleado1()
    condicional = emple.baja(dept)
    condicional1 = {
        'condicional1': condicional,
        'crud': 'BAJA'
    }
    return render(request, "data/templateResultado.html", condicional1)


def modificar1(request):
    dept = request.POST['dept_no']
    loc = request.POST['loc']
    emple = Empleado1()
    condicional = emple.modificar(dept, loc)
    condicional1 = {
        'condicional1': condicional,
        'crud': 'MODIFICAR'
    }
    return render(request, "data/templateResultado.html", condicional1)


def listar1(request):
    emple = Empleado1()
    condicional = emple.devolverdato()
    condicional1 = {
        'condicional1': condicional,
        'crud': 'LISTAR'
    }
    return render(request, "data/template5Listado.html", condicional1)
