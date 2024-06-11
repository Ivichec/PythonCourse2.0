from datetime import datetime
from math import floor

fechaNacimiento1 = input('Escribe tu fecha de nacimiento (dd/mm/yyyy): ')
fechaNacimiento = datetime.strptime(fechaNacimiento1, '%d/%m/%Y')

dias = ("Sábado","Domingo","Lunes","Martes","Miercoles","Jueves","Viernes")
if fechaNacimiento.month == 1:
    month = 13
    year = fechaNacimiento.year - 1
elif fechaNacimiento.month == 2:
    month = 14
    year = fechaNacimiento.year - 1
else:
    month = fechaNacimiento.month
resultadoM = int(((month + 1) * 3)/5)
resultadoA0 = int(year / 4)
resultadoA1 = int(year / 100)
resultadoA2 = int(year / 400)
resultadoT = int(fechaNacimiento.day + (month * 2) + year + resultadoM + resultadoA0 - resultadoA1 + resultadoA2 + 2)
print(floor(resultadoT))
resultado = int(resultadoT / 7)
resultadoF = int(resultadoT - (resultado * 7))
print(resultadoF)
print('Naciste este dia de la semana: ',dias[resultadoF])