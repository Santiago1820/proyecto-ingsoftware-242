import tkinter as Tk
import pages.controller as controller
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class Dashboard(Tk.Frame):
    def __init__(self, parent):
        Tk.Frame.__init__(self, parent)
        self.parent = parent

        self.label = Tk.Label(self, text="¡Hola Mundo!")
        self.label.pack()

        self.login_button = Tk.Button(self, text="Salir", command=controller.cerrar_app)
        self.login_button.configure(bg="#FFFFFF", fg="black")
        self.login_button.pack()

    def admin(self):
        self.parent.withdraw()
        controller.show_tareas()

if __name__ == "__main__":
    # Creamos un estilo y aplicamos el tema 'darkly'
    root = Tk.Tk()
    dashboard_page = Dashboard(root)
    dashboard_page.pack()
    root.mainloop()