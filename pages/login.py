import tkinter as Tk
from tkinter import messagebox, ttk
import pages.mostrar as mostrar
from pages.db import conexion
from pages.encrypt import encriptar
from ttkbootstrap.constants import *

class LoginPage(Tk.Frame):
    def __init__(self, parent):
        Tk.Frame.__init__(self, parent)
        self.parent = parent
        
        self.username_label = ttk.Label(self, text="Usuario:", bootstyle="light")
        self.username_label.pack()
        self.username_entry = ttk.Entry(self, bootstyle="light")
        self.username_entry.pack()

        self.password_label = ttk.Label(self, text="Contraseña:", bootstyle="light")
        self.password_label.pack()
        self.password_entry = ttk.Entry(self, show="*", bootstyle="light")
        self.password_entry.pack()
 
        self.type_user = ttk.Combobox(values=["Administrador", "Usuario"], state="readonly")
        self.type_user.current(1)
        self.type_user.pack()

        self.login_button = ttk.Button(self, text="Iniciar sesión", bootstyle=(LIGHT, OUTLINE), cursor="hand2", command=self.login)
        self.login_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        tipo = self.type_user.get()

        if not username or not password:
            messagebox.showerror("Error", "Por favor ingrese usuario y contraseña.")
            return

        # Encriptar la contraseña ingresada por el usuario
        contraseña_encriptada = encriptar(password)

        # Establecer conexión con la base de datos
        conectar = conexion()
        cursor = conectar.cursor()
        cursor.execute(f"SELECT * FROM usuarios WHERE usuario = '{username}' AND password = '{contraseña_encriptada}'")
        respuesta = cursor.fetchone()

        # Si la conexion es correcta vamos a dirigir a dash
        if respuesta:
            if tipo == "Administrador":
                cursor.execute(f"SELECT estudios FROM usuarios WHERE usuario = '{username}' AND estudios = '{tipo}'")
                tipo_usr = cursor.fetchone()
                mostrar.cerrar_conexion()
                if tipo_usr:
                    self.parent.withdraw()
                    mostrar.show_admin()
                else:
                    messagebox.showerror("Error", "No eres Administrador")
            else:
                self.parent.withdraw()
                mostrar.show_dash()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

if __name__ == "__main__":
    root = Tk.Tk()
    LoginPage(root).pack()
    root.mainloop()
