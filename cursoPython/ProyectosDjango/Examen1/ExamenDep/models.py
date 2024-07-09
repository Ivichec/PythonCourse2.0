import cx_Oracle


class Dept:

    def __init__(self):
        self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

    def listarDept(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT * FROM dept")

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor

    def borrarFila(self, dept_no):
        cursor = self.connection.cursor()
        try:
            consulta = "DELETE FROM DEPT WHERE DEPT_NO = :p1"
            cursor.execute(consulta, (dept_no,))
            self.connection.commit()
            return True
        except cx_Oracle.DatabaseError as error:
            print("Error: ", error)
            return False
        finally:
            cursor.close()

    def listarDeptNo(self, dept_no):
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT * FROM dept WHERE DEPT_NO = :p1", (dept_no,))
            resultados = cursor.fetchall()
        except self.connection.Error as error:
            print("Error: ", error)

        return resultados

    def modificar(self, newdept, dept_no, nombre, loc):
        cursor = self.connection.cursor()
        try:
            consulta = "UPDATE DEPT SET DEPT_NO = :p1,DNOMBRE = :p2, LOC = :p3 WHERE DEPT_NO = :p4"
            cursor.execute(consulta, (newdept, nombre, loc, dept_no))
            self.connection.commit()
            return True
        except cx_Oracle.DatabaseError as error:
            print("Error: ", error)
            return False
        finally:
            cursor.close()

    def nuevoDept(self, dept_no,dnombre,loc):
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
