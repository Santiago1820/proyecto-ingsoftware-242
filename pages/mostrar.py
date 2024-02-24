import tkinter as Tk
import pages.dash as dash, pages.register as register, pages.admin as admin
import sys
from pages.db import conexion

nombresys = "Sistema - Registro v1.0"
conectar = conexion()
cursor = conectar.cursor()

def cerrar_conexion():
    cursor.close()
    conectar.close()

def show_register():
    new_root = Tk.Tk()
    new_root.geometry("1200x750")
    new_root.title("Registrarse")
    new_root.resizable(0,0)
    new_root.protocol("WM_DELETE_WINDOW", no_cerrar)
    new_root.attributes('-fullscreen', True)
    admin_page = register.registro(new_root)
    admin_page.pack()
    new_root.mainloop()

def show_dash():
    new_root = Tk.Tk()
    new_root.geometry("1200x750")
    new_root.resizable(0,0)
    new_root.protocol("WM_DELETE_WINDOW", no_cerrar)
    new_root.attributes('-fullscreen', True)
    new_root.title(f"{nombresys}")
    dash_page = dash.Dashboard(new_root)
    dash_page.pack()
    new_root.mainloop()

def show_admin():
    new_root = Tk.Tk()
    new_root.geometry("1200x750")
    new_root.resizable(0,0)
    new_root.protocol("WM_DELETE_WINDOW", no_cerrar)
    new_root.attributes('-fullscreen', True)
    new_root.title(f"{nombresys}")
    admin_page = admin.Admin(new_root)
    admin_page.pack()
    new_root.mainloop()

def cerrar_app():
    sys.exit()


def no_cerrar():
    pass