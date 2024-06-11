from math import floor, ceil

print('redondeando')
numero1 = 6.67
print('Division')
numero3 = 20
numero2 = 3

print('Resultado sin redondear', round(numero3/numero2,2))
print('Resultado redondeado a la menor', floor(numero3/numero2))
print('Resultado redondeado a la mayor', ceil(numero3/numero2))

edad = 40
if edad == 39:
    print('Tienes 39 años')
else:
    print('No tienes 39 años')



for i in range(0,5):
    numero = input('Escribe un numero')
    if int(numero) % 2 == 0:
        print('El numero es par')
    else:
        print('Es numero es impar')
