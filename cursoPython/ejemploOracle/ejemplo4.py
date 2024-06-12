import cx_Oracle

connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

cursor = connection.cursor()
try:

    ConsultaBaja = "INSERT INTO DEPT(DEPT_NO,DNOMBRE,LOC) VALUES(:param1,:param2,:param3)"

    NumeroDept = input("Número de departamento:")
    nombre = input("Número de nombre de departamento:")
    localizacion = input("Número de localizacion del departamento:")

    cursor.execute(ConsultaBaja, (NumeroDept,nombre,localizacion))

    if cursor.rowcount > 0:
        print("Registro insertado satisfactoriamente")
    else:
        print("Datos erroneos")

    connection.commit()


except connection.Error as error:
    print("Error: ", error)
cursor.close()
connection.close()