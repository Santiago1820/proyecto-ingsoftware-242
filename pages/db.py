import mysql.connector
def conexion ():
    try:
        conexion = mysql.connector.connect(
            host = "peb.h.filess.io",
            user = "IngSoftware_sizeherdas",
            password = "redes_password",
            database = "IngSoftware_sizeherdas",
            port = "3307"
        )
        return conexion
    except mysql.connector.Error as e:
        print(f"Error al conectar a la BD: {e}")
        return None