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

        self.login_button = Tk.Button(self, text="Button 1", command=self.admin)
        self.login_button.pack(side=LEFT, padx=5, pady=10)

    def admin(self):
        self.parent.withdraw()
        controller.show_tareas()

if __name__ == "__main__":
    root = Tk.Tk()
    dashboard_page = Dashboard(root)
    dashboard_page.pack()
    root.mainloop()