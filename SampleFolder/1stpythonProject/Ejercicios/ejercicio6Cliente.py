from Ejercicios.ejercicio6ClaseDni import Dni

numeroDni = int(input('Escribe tu numero de dni: '))
miDni = Dni(numeroDni)
letra = miDni.letraDni()
print(f"La letra de tu DNI es: {letra}")
