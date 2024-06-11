import cx_Oracle

connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

cursor = connection.cursor()
try:

    cursor.execute("SELECT DOCTOR_NO,APELLIDO,ESPECIALIDAD FROM DOCTOR WHERE upper(ESPECIALIDAD) = 'CARDIOLOGIA' ")
    results = cursor.fetchall()
    # Imprime los resultados
    for row in results:
        print(row)
    print("Lista de empleados:")
    print("---------------------------------------")

    for DOCTOR_NO, APELLIDO, ESPECIALIDAD in cursor:
        print("Número empleado:", DOCTOR_NO, "Apellido:", APELLIDO, "Especialidad:", ESPECIALIDAD)


except connection.Error as error:
    print("Error: ", error)

connection.close()