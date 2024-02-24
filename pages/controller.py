import tkinter as Tk
import pages.dash as dash, pages.register as register, pages.admin as admin
import sys
from pages.db import conexion
from config import *

# Definimos las variables de configuración
namesys = nombre()
# Funcion para conectarnos a nuestra base de datos utilizando nuestro archivod e conexion bd.py
conectar = conexion()
cursor = conectar.cursor()

# Funcion para cerrar la sesion de MySQL
def cerrar_conexion():
    cursor.close()
    conectar.close()

# Metodo para mostrarnuestra ventana de registro
def show_register():
    # Creamos nuestra nueva ventana
    new_root = Tk.Tk()
    # Titulo de nuestra ventana
    new_root.title("Registrarse")
    # Cancelamos el evento cerrar
    new_root.protocol("WM_DELETE_WINDOW", no_cerrar)
    # Mostramos la pagina en modo pantalla completa
    new_root.attributes('-fullscreen', True)
    # Creamos nuestro registro y a imprimimos
    register_page = register.Registro(new_root)
    register_page.pack()
    # Mostramos nuestro contenido
    new_root.mainloop()

def show_dash():
    new_root = Tk.Tk()
    new_root.protocol("WM_DELETE_WINDOW", no_cerrar)
    new_root.attributes('-fullscreen', True)
    new_root.title(f"{namesys}")
    dash_page = dash.Dashboard(new_root)
    dash_page.pack()
    new_root.mainloop()

def show_admin():
    new_root = Tk.Tk()
    new_root.protocol("WM_DELETE_WINDOW", no_cerrar)
    new_root.attributes('-fullscreen', True)
    new_root.title(f"{namesys}")
    admin_page = admin.Admin(new_root)
    admin_page.pack()
    new_root.mainloop()

# Funcion para cerrar el sistema completo
def cerrar_app():
    sys.exit()

# Cancelamos el cerrar con un pass para pasar la accion
def no_cerrar():
    pass