import cx_Oracle

class Formulario:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

    def insertdato(self, hospNombre):
        cursor = self.connection.cursor()
        try:
            consulta = (
                "SELECT * FROM EMP WHERE OFICIO = :p1"
            )
            cursor.execute(consulta,(hospNombre,))
            results = cursor.fetchall()
            return results  # Return the fetched results
        except cx_Oracle.DatabaseError as error:
            print("Error: ", error)
            return None
        finally:
            cursor.close()