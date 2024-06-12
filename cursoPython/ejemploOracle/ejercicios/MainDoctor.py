from metodosDoctor import Doctor
verdad = True
while verdad:
    numero = int(input("Pulsa 1 para dar de alta a un doctor \n"
              "Pulsa 2 para dar de baja a un doctor \n"
              "Pulsa 3 para modificar a un doctor \n"
              "Pulsa 4 para listar la tabla doctor \n"
              "Pulsa 5 para salir"))
    miDoctor = Doctor(45,696,'Checa I.','Ginecologia',10000)
    match numero:
        case 1:
            miDoctor.altaDoctor()
        case 2:
            miDoctor.bajaDoctor()
        case 3:
            miDoctor.modificarSalarioDoctor(1000)
        case 4:
            miDoctor.listarDoctores()
        case 5:
            verdad = miDoctor.salir()