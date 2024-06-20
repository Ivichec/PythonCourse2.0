import cx_Oracle


class Empleado1:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

    def insertdato(self, dept_no,dnombre,loc):
        cursor = self.connection.cursor()
        try:
            consulta = "INSERT INTO DEPT VALUES(:p1, :p2, :p3)"
            cursor.execute(consulta, (dept_no, dnombre, loc))
            self.connection.commit()
            return True
        except cx_Oracle.DatabaseError as error:
            print("Error: ", error)
            return False
        finally:
            cursor.close()
    def baja(self, dept_no):
        cursor = self.connection.cursor()
        try:
            consulta = "DELETE FROM EMP WHERE DEPT_NO = :p1"
            cursor.execute(consulta, (dept_no,))
            self.connection.commit()
            return True
        except cx_Oracle.DatabaseError as error:
            print("Error: ", error)
            return False
        finally:
            cursor.close()
    def modificar(self, dept_no,loc):
        cursor = self.connection.cursor()
        try:
            consulta = "UPDATE DEPT SET LOC = :p2 WHERE DEPT_NO = p1"
            cursor.execute(consulta, (dept_no, loc))
            self.connection.commit()
            return True
        except cx_Oracle.DatabaseError as error:
            print("Error: ", error)
            return False
        finally:
            cursor.close()
    def devolverdato(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT * FROM dept")

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor