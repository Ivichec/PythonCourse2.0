import cx_Oracle


class Formulario:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

    def insertdato(self, nom, ape1, ape2, dom, ciu, sex, sis,com):
        cursor = self.connection.cursor()
        try:
            consulta = "INSERT INTO clientesAlumnos VALUES(:p1, :p2, :p3, :p4, :p5, :p6, :p7, :p8)"
            cursor.execute(consulta, (nom, ape1, ape2, dom, ciu, sex, sis,com))
            self.connection.commit()
            return True
        except cx_Oracle.DatabaseError as error:
            print("Error: ", error)
            return False
        finally:
            cursor.close()