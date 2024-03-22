import ttkbootstrap
from pages import login

# Diseño de nuestra ventana la ca le daremos el tema de darkly de la libreria ttkbootstrap, le estableceremos el valor por default de la ventana y el titulo de la ventana, a su vez le pondremos el icono a nuestra ventana
root = ttkbootstrap.Window(themename="darkly")
root.title("Iniciar Sesión")
root.geometry("1200x750")

# Mostrar la página de login por defecto
login_page = login.LoginPage(root)
login_page.pack()

root.mainloop() 