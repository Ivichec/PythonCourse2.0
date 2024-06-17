from claseEmp import Empleado
verdad = True
while verdad:
    numero = int(input("Pulsa 1 para buscar salario y comision \n"
              "Pulsa 2 para modificar salario y comision \n"
              "Pulsa 3 para salir"))
    miEmp = Empleado()
    match numero:
        case 1:
            num = int(input("Introduce el emp_no: "))
            print("Salario: " + str(miEmp.buscar(num)[0]))
            print("Comision: " + str(miEmp.buscar(num)[1]))
        case 2:
            sal = int(input("Introduce el nuevo salario: "))
            comi = int(input("Introduce la nueva comision: "))
            num = int(input("Introduce el emp_no: "))
            miEmp.modificar(sal,comi,num)
            if int(miEmp.modificar(sal,comi,num)[0]) >= 1:
                print("Doctores borrados: " + str(miEmp.modificar(sal,comi,num)[0]))
            else:
                print("Ningun doctor borrado")
        case 3:
            verdad = False