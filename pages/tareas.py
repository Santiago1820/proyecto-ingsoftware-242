import tkinter as Tk
import pages.controller as controller

class Tareas(Tk.Frame):
    def __init__(self, parent):
        Tk.Frame.__init__(self, parent)
        self.parent = parent

        self.label = Tk.Label(self, text="Esto es tareas")
        self.label.pack()

        self.login_button = Tk.Button(self, text="Ir a admin", command=self.admin)
        self.login_button.pack()

    def admin(self):
        self.parent.withdraw()
        controller.show_admin()

if __name__ == "__main__":
    root = Tk.Tk()
    tareas_page = Tareas(root)
    tareas_page.pack()
    root.mainloop()