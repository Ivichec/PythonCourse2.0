import cx_Oracle

connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

cursor = connection.cursor()
try:

    dp = input("Número de inscripcion del enfermo: ")
    sex = cursor.var(cx_Oracle.STRING)
    ape = cursor.var(cx_Oracle.STRING)

    args = (sex,ape, dp)
    cursor.callproc('DevolverEnfermo', args)
    print(sex.getvalue())
    print(ape.getvalue())



except connection.Error as error:
    print("Error: ", error)
cursor.close()
connection.close()