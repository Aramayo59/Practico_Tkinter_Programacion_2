import tkinter as tk  # Importa la biblioteca tkinter para crear la interfaz gráfica.

# Función que añade la película ingresada a la lista.
def añadir_pelicula():
    pelicula = pelicula_var.get()  # Obtiene el título de la película del campo de entrada.
    if pelicula:  # Verifica que el campo no esté vacío.
        listbox.insert(tk.END, pelicula)  # Inserta el título en el listbox.
        pelicula_var.set("")  # Resetea el campo de entrada.

# Crear la ventana principal.
root = tk.Tk()
root.title("Películas")  # Título de la ventana.

# Configuración del tamaño de la ventana.
root.geometry("550x450")  # Tamaño inicial de la ventana.
root.minsize(350, 350)  # Tamaño mínimo de la ventana.

# Colores utilizados en la interfaz.
bg_color = "#2e2e2e"  # Fondo gris oscuro.
entry_bg = "#424242"  # Fondo gris oscuro para el campo de entrada.
button_bg = "#607d8b"  # Color azul grisáceo para los botones.
button_fg = "#ffffff"  # Texto de los botones en blanco.
listbox_bg = "#37474f"  # Fondo gris azulado oscuro para la lista.
listbox_fg = "#ffffff"  # Texto en blanco para la lista.
label_fg = "#b0bec5"  # Color gris claro para las etiquetas.

# Aplica el color de fondo a la ventana principal.
root.configure(bg=bg_color)

# Variable que almacena el título de la película ingresada.
pelicula_var = tk.StringVar()

# Etiqueta para el campo de entrada de la película.
tk.Label(root, text="Escribe el título de una película", font=("Arial", 12), bg=bg_color, fg=label_fg).pack(pady=(10, 5))

# Campo de entrada donde el usuario escribe el título de la película.
tk.Entry(root, textvariable=pelicula_var, font=("Arial", 12), bg=entry_bg, fg="#ffffff", width=30).pack(pady=(0, 10))

# Etiqueta para la lista de películas.
tk.Label(root, text="Películas", font=("Arial", 12), bg=bg_color, fg=label_fg).pack(pady=(10, 5))

# Lista donde se mostrarán los títulos de las películas añadidas.
listbox = tk.Listbox(root, font=("Arial", 12), width=40, height=10, bg=listbox_bg, fg=listbox_fg, borderwidth=2, relief="solid")
listbox.pack(pady=(0, 10))

# Botón para añadir una película a la lista.
tk.Button(root, text="Añadir", command=añadir_pelicula, font=("Arial", 12), bg=button_bg, fg=button_fg).pack(pady=(10, 10))

# Inicia el bucle principal de la aplicación.
root.mainloop()
