from django.shortcuts import render
from ExamenDep.models import Dept


def index(request):
    emple = Dept()
    datos = emple.listarDept()
    datosDept = {
        'condicional1': datos
    }
    return render(request, "Dept/Index.html", datosDept)


def baja(request):
    dept = request.GET['dept_no']
    emple = Dept()
    emple.borrarFila(dept)
    datos = emple.listarDept()
    datosDept = {
        'condicional1': datos
    }
    return render(request, "Dept/Index.html", datosDept)


def modificar(request):
    dept = request.GET['dept_no']
    emple = Dept()
    datos = emple.listarDeptNo(dept)
    datosDept = {
        'condicional1': datos
    }
    return render(request, "Dept/Editar.html", datosDept)


def editarDeptNo(request):
    newdept = request.POST['newdept']
    dept = request.POST['olddept']
    nom = request.POST['nom']
    loc = request.POST['loc']
    emple = Dept()
    booleano = emple.modificar(newdept, dept,nom,loc)
    datos = emple.listarDept()
    datosDept = {
        'condicional1': datos
    }
    if booleano:
        return render(request, "Dept/Index.html", datosDept)
    else:
        return render(request, "Dept/IndexError.html", datosDept)


def alta(request):
    return render(request, "Dept/NewDept.html")

def darAlta(request):
    dept = request.POST['deptNo']
    nom = request.POST['nom']
    loc = request.POST['loc']
    emple = Dept()
    booleano =emple.nuevoDept(dept,nom,loc)
    datos = emple.listarDept()
    datosDept = {
        'condicional1': datos,
    }
    if booleano:
        return render(request, "Dept/Index.html",datosDept)
    else:
        return render(request, "Dept/IndexError.html", datosDept)