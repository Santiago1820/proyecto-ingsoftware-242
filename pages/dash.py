import tkinter as Tk
import pages.controller as controller
import ttkbootstrap as ttk

class Dashboard(Tk.Frame):
    def __init__(self, parent):
        Tk.Frame.__init__(self, parent)
        self.parent = parent

        self.label = Tk.Label(self, text="¡Hola Mundo!")
        self.label.pack()

        self.login_button = ttk.Button(self, text="Test", bootstyle="secondary", command=self.admin)
        self.login_button.pack()

    def admin(self):
        self.parent.withdraw()
        controller.show_tareas()

if __name__ == "__main__":
    root = Tk.Tk()
    dashboard_page = Dashboard(root)
    dashboard_page.pack()
    root.mainloop()