from pages.encrypt import encriptar
from pages.db import conexion
from tkinter import messagebox
import tkinter as Tk

class Registro(Tk.Frame):
    def __init__(self, parent):
        Tk.Frame.__init__(self, parent)
        self.parent = parent

        self.username_label = Tk.Label(self, text="Usuario:")
        self.username_label.pack()
        self.username_entry = Tk.Entry(self)
        self.username_entry.pack()

        self.password_label = Tk.Label(self, text="Contraseña:")
        self.password_label.pack()
        self.password_entry = Tk.Entry(self, show="*")
        self.password_entry.pack()

        self.name_label = Tk.Label(self, text="Nombre(S):")
        self.name_label.pack()
        self.name_entry = Tk.Entry(self)
        self.name_entry.pack()

        self.login_button = Tk.Button(self, text="Registrarme", command=self.registro)
        self.login_button.pack()

    def registro(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        correo = "Null"
        #password = contraseña.get()
        name = self.name_entry.get()

        contraseña_encriptada = encriptar(password)

        conectar = conexion()
        cursor = conectar.cursor()
        cursor.execute(f"INSERT INTO usuarios (usuario, nombre, email, password) VALUES ('{username}', '{name}', '{correo}', '{contraseña_encriptada}')")
        conexion.comit
        cursor.close
        conexion.close()

        messagebox.showinfo("Te has registrado correctamente")

if __name__ == "__main__":
    root = Tk.Tk()
    Register_page = Registro(root)
    Register_page.pack()
    root.mainloop()