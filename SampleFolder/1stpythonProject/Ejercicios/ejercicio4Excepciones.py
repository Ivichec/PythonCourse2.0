premios = [166116.06,111123.48,33343.54,1544.22,123.12,66.37,44.89,15.91]
def premio(num):
    try:
        return premios[num]
    except IndexError:
        print("Error el numero no esta en la lista")

print("---ACCESO A LOS PRIMEROS PREMIOS DEL EUROMILLON")
numero = int(input("Introduzca el numero del premio a mostrar: "))
print(premio(numero))