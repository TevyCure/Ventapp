from conexion import Conexion


def inventarioBBDD():
    try:
        #REALIZAR LA CONEXION A ORACLE CON cx_Oracle.connect
        ''' connection = cx_Oracle.connect(
            user='TEVY',
            password='molinosdeviento',
            dsn='localhost:1521/xe',
            encoding='UTF-8'
        ) '''
    
        #se hace un select en los productos
        Conexion.cursor.execute("SELECT * FROM PRODUCTO")
        #con fetchall se hace una lista con todo lo obtenido de usuarios
        rows = Conexion.cursor.fetchall()
        print(rows)
        return rows
    except:
        pass
    
