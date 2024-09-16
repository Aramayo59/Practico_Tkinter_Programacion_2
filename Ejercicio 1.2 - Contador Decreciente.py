import tkinter as tk  # Importa la biblioteca tkinter para crear la interfaz gráfica.

# Función para decrementar el valor del contador.
def decrementar():
    contador.set(contador.get() - 1)  # Resta 1 al valor actual del contador y lo actualiza.

# Crear la ventana principal de la aplicación.
root = tk.Tk()
root.title("ContDecreciente")  # Establece el título de la ventana.
root.geometry("400x250")  # Define el tamaño de la ventana (400x250 píxeles).
root.configure(bg="#1a1a1a")  # Configura el color de fondo de la ventana (negro oscuro).

root.resizable(False, False)  # Evita que la ventana sea redimensionada por el usuario.

# Crear una variable tkinter de tipo entero para almacenar el valor del contador.
contador = tk.IntVar()
contador.set(88)  # Inicializa el contador en 88.

# Crear un contenedor (frame) para organizar los widgets dentro de la ventana.
frame = tk.Frame(root, bg="#1a1a1a")
frame.place(relx=0.5, rely=0.5, anchor="center")  # Coloca el frame en el centro de la ventana.

# Crear una etiqueta que muestra el texto "Contador".
tk.Label(frame, text="Contador", font=("Arial", 14), bg="#1a1a1a", fg="#cc0000").pack(pady=5)
# El fondo es negro oscuro y el texto de la etiqueta es rojo.

# Crear un campo de entrada para mostrar el valor del contador (solo lectura).
tk.Entry(frame, textvariable=contador, state="readonly", font=("Arial", 14), justify="center", bg="#cc0000", fg="black").pack(pady=5)
# El fondo del campo de entrada es rojo, y el texto es negro. El estado de solo lectura impide que el usuario edite el valor manualmente.

# Crear un botón que decrementa el contador al hacer clic.
tk.Button(frame, text="-", font=("Arial", 14), command=decrementar, bg="#cc0000", fg="white", activebackground="#b30000", activeforeground="white").pack(pady=10)
# El botón tiene un texto "-", con fondo rojo y texto blanco. El color de fondo cambia a un rojo más oscuro cuando el botón está activo.

# Inicia el bucle principal de la ventana.
root.mainloop()
