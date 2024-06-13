import cx_Oracle

connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

cursor = connection.cursor()
try:

    numEmp = input("Numero de empleado al que quieres borrar: ")

    cursor.callproc("DELETEPLAN", (numEmp,))

    if cursor.rowcount > 0:
        print("Registro insertado satisfactoriamente")
    else:
        print("Dato no encontrado")



except connection.Error as error:
    print("Error: ", error)
cursor.close()
connection.close()