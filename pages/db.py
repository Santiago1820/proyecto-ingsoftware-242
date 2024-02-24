import mysql.connector
def conexion ():
    try:
        conexion = mysql.connector.connect(
            host = "sql3.freemysqlhosting.net",
            user = "sql3680163",
            password = "PJ6R8RqwBc",
            database = "sql3680163"
        )
        return conexion
    except mysql.connector.Error as e:
        print(f"Error al conectar a la BD: {e}")
        return None