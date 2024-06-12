import cx_Oracle
class Doctor:
    hospital_cod = 0
    doctor_no = 0
    apellido = ""
    especialidad = ""
    salario = 0
    def __init__(self, h,d,a,e,s):
        self.hospital_cod = h
        self.doctor_no = d
        self.apellido = a
        self.especialidad = e
        self.salario = s
    def altaDoctor(self):
        connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")
        cursor = connection.cursor()
        try:
            ConsultaBaja = "INSERT INTO DOCTOR VALUES(:param1,:param2,:param3,:param4,:param5)"
            cursor.execute(ConsultaBaja, (self.hospital_cod, self.doctor_no, self.apellido, self.especialidad, self.salario))
            connection.commit()
        except connection.Error as error:
            print("Error: ", error)
        connection.close()
    def bajaDoctor(self):
        connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")
        cursor = connection.cursor()
        try:
            ConsultaBaja = "Delete from doctor where doctor_no=:param1"
            cursor.execute(ConsultaBaja, (self.doctor_no,))
            connection.commit()
        except connection.Error as error:
            print("Error: ", error)
        connection.close()
    def modificarSalarioDoctor(self,num):
        connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")
        cursor = connection.cursor()
        try:
            ConsultaBaja = "UPDATE DOCTOR SET SALARIO =:p1 WHERE DOCTOR_NO =:p2"
            cursor.execute(ConsultaBaja, (num,self.doctor_no))
            connection.commit()
        except connection.Error as error:
            print("Error: ", error)

        connection.close()
    def listarDoctores(self):
        connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM DOCTOR")
            results = cursor.fetchall()
            # Imprime los resultados
            for row in results:
                print(row)
            print("Lista de empleados:")
            print("---------------------------------------")
            for HOSPITAL_COD, DOCTOR_NO, APELLIDO, ESPECIALIDAD, SALARIO in cursor:
                print("Codigo hospital: ", HOSPITAL_COD,"Número empleado: ", DOCTOR_NO, "Apellido: ", APELLIDO, "Especialidad: ", ESPECIALIDAD,"Salario: ", SALARIO)
        except connection.Error as error:
            print("Error: ", error)
        connection.close()
    def salir(self):
        return False


