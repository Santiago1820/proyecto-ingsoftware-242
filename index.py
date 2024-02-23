import ttkbootstrap
import login

root = ttkbootstrap.Window(themename="darkly")
root.title("Iniciar Sesión")
root.geometry("1200x750")

# Mostrar la página de login por defecto
login_page = login.LoginPage(root)
login_page.pack()

root.mainloop()