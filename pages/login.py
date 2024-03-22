import tkinter as Tk
from tkinter import messagebox, ttk
import pages.controller as controller
from pages.db import conexion
from pages.encrypt import encriptar
from ttkbootstrap.constants import *

class LoginPage(Tk.Frame):
    def __init__(self, parent):
        Tk.Frame.__init__(self, parent)
        self.parent = parent
        
        # Crear etiqueta y campo de entrada para el nombre de usuario
        self.username_label = ttk.Label(self, text="Usuario:", bootstyle="light")
        self.username_label.pack()
        self.username_entry = ttk.Entry(self, bootstyle="light")
        self.username_entry.pack()

        # Crear etiqueta y campo de entrada para la contraseña
        self.password_label = ttk.Label(self, text="Contraseña:", bootstyle="light")
        self.password_label.pack()
        self.password_entry = ttk.Entry(self, show="*", bootstyle="light")  # El parámetro 'show' oculta la entrada
        self.password_entry.pack()
 
        # Crear menú desplegable para seleccionar el tipo de usuario
        self.type_user = ttk.Combobox(values=["Administrador", "Usuario"], state="readonly")
        self.type_user.current(1)  # Establecer el valor predeterminado como "Usuario"
        self.type_user.pack()

        # Crear botón para iniciar sesión
        self.login_button = ttk.Button(self, text="Iniciar sesión", bootstyle=(LIGHT, OUTLINE), cursor="hand2", command=self.login)
        self.login_button.pack()

    def login(self):
        # Obtener el nombre de usuario, contraseña y tipo de usuario ingresados por el usuario
        username = self.username_entry.get()
        password = self.password_entry.get()
        tipo = self.type_user.get()

        # Verificar si se ingresaron tanto el nombre de usuario como la contraseña
        if not username or not password:
            messagebox.showerror("Error", "Por favor ingrese usuario y contraseña.")
            return

        # Encriptar la contraseña ingresada por el usuario
        contraseña_encriptada = encriptar(password)

        # Establecer conexión con la base de datos
        conectar = conexion()
        cursor = conectar.cursor()

        # Ejecutar consulta para verificar el nombre de usuario y contraseña
        cursor.execute(f"SELECT * FROM usuarios WHERE usuario = '{username}' AND password = '{contraseña_encriptada}'")
        respuesta = cursor.fetchone()

        # Si la consulta devuelve un resultado válido
        if respuesta:
            # Verificar el tipo de usuario
            if tipo == "Administrador":
                cursor.execute(f"SELECT tipo FROM usuarios WHERE usuario = '{username}' AND tipo = '{tipo}'")
                tipo_usr = cursor.fetchone()
                controller.cerrar_conexion()
                # Si el usuario es administrador, mostrar la ventana de administrador
                if tipo_usr:
                    self.parent.withdraw()
                    controller.show_admin()
                else:
                    messagebox.showerror("Error", "No eres Administrador")
            else:
                # Si el usuario no es administrador, mostrar la ventana de dashboard
                self.parent.withdraw()
                controller.show_dash()
        else:
            # Si la consulta no devuelve un resultado válido, mostrar mensaje de error
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

if __name__ == "__main__":
    # Crear la ventana principal de la aplicación
    root = Tk.Tk()
    # Agregar la página de inicio de sesión a la ventana
    LoginPage(root).pack()
    # Iniciar el bucle principal para que la interfaz de usuario sea interactiva
    root.mainloop()