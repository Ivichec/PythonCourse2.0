import cx_Oracle

class Formulario:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

    def insertdato(self, hospNombre):
        cursor = self.connection.cursor()
        try:
            consulta = (
                "SELECT DOCTOR.APELLIDO, DOCTOR.ESPECIALIDAD, DOCTOR.SALARIO FROM HOSPITAL INNER JOIN DOCTOR ON HOSPITAL.HOSPITAL_COD = DOCTOR.HOSPITAL_COD WHERE HOSPITAL.NOMBRE IN ("+hospNombre+")"
            )
            cursor.execute(consulta)
            results = cursor.fetchall()
            return results  # Return the fetched results
        except cx_Oracle.DatabaseError as error:
            print("Error: ", error)
            return None
        finally:
            cursor.close()
