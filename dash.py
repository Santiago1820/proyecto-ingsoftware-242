import tkinter as Tk
import mostrar

class Dashboard(Tk.Frame):
    def __init__(self, parent):
        Tk.Frame.__init__(self, parent)
        self.parent = parent

        self.label = Tk.Label(self, text="¡Hola Mundo!")
        self.label.pack()

        self.login_button = Tk.Button(self, text="Ir a admin", command=mostrar.cerrar_app)
        self.login_button.pack()

    def admin(self):
        self.parent.withdraw()
        mostrar.show_admin()

if __name__ == "__main__":
    root = Tk.Tk()
    dashboard_page = Dashboard(root)
    dashboard_page.pack()
    root.mainloop()