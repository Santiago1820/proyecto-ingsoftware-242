import tkinter as Tk
import pages.controller as controller

class Admin(Tk.Frame):
    def __init__(self, parent):
        Tk.Frame.__init__(self, parent)
        self.parent = parent

        self.label = Tk.Label(self, text="¡Hola Mundo!, este es admin")
        self.label.pack()

        self.login_button = Tk.Button(self, text="Ir a admin", command=controller.cerrar_app)
        self.login_button.pack()


if __name__ == "__main__":
    root = Tk.Tk()
    Admin_page = Admin(root)
    Admin_page.pack()
    root.mainloop()