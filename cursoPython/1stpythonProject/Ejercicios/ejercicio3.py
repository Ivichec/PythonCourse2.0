def narcicista(num):
    num2 = 0
    potencia = len(num)

    for i in range(potencia):
        num2 = num2 + pow(int(num[i]), potencia)

    if num2 == int(num):
        resultado = True
    else:
        resultado = False

    return resultado

def conjeturaCollatz(numero):
    resultado = ""
    while numero != 1:
        resultado += "\n"
        if (numero % 2 == 0):
            numero = numero / 2
        else:
            numero = (numero * 3) + 1
        resultado += str(numero)
        resultado += "\n"
    return resultado

verdad = True
while verdad:
    numero = int(input("Pulsa 1 para comprobar un numero Narcicista \n"
              "Pulsa 2 para mostrar la conjetura de Collatz \n"
              "Pulsa 3 para salir"))
    if numero == 1:
        numeroN = input("Escribe el numero a comprobar: ")
        print(narcicista(numeroN))
    elif numero == 2:
        numeroC = int(input("Escribe el numero a comprobar: "))
        print(conjeturaCollatz(numeroC))
    else:
       verdad = False