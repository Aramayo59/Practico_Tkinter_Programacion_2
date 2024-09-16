import tkinter as tk  # Importar la biblioteca tkinter para la interfaz gráfica.

# Función para incrementar el valor del contador en 1.
def incrementar():
    """Incrementa el valor del contador en 1."""
    contador.set(contador.get() + 1)

# Función para decrementar el valor del contador en 1.
def decrementar():
    
    contador.set(contador.get() - 1)

# Función para resetear el contador a 0.
def resetear():
    
    contador.set(0)

# Crear la ventana principal de la aplicación.
root = tk.Tk()
root.title("Contador")  # Título de la ventana.
root.geometry("700x400")  # Tamaño de la ventana (700x400 píxeles).
root.configure(bg="#f0f8ff")  # Fondo de la ventana de color azul claro (#f0f8ff).

root.resizable(False, False)  # Evita que la ventana sea redimensionada.

# Crear una variable tkinter de tipo entero para almacenar el valor del contador.
contador = tk.IntVar()
contador.set(0)  # Inicializa el contador en 0.

# Crear un frame principal que contendrá todos los widgets.
main_frame = tk.Frame(root, bg="#f0f8ff", padx=20, pady=20)  # Frame con padding y color de fondo azul claro.
main_frame.pack(expand=True, fill=tk.BOTH)  # Empaqueta el frame, permitiendo que se expanda en ambas direcciones.

# Etiqueta para el texto "Contador".
label = tk.Label(main_frame, text="Contador", bg="#f0f8ff", font=("Helvetica", 20, "bold"))
label.grid(row=0, column=0, columnspan=2, pady=10)  # Coloca la etiqueta en la primera fila y ocupa 2 columnas.

# Entrada para mostrar el valor del contador (solo lectura).
entrada = tk.Entry(main_frame, textvariable=contador, state="readonly", font=("Helvetica", 40, "bold"), bg="white", bd=2, relief="solid")
entrada.grid(row=1, column=0, columnspan=2, pady=10, padx=10)  # Entrada centrada con padding.

# Crear un frame para los botones.
button_frame = tk.Frame(main_frame, bg="#f0f8ff")  # Frame para organizar los botones.
button_frame.grid(row=2, column=0, columnspan=2, pady=10)  # Coloca el frame en la tercera fila, ocupando 2 columnas.

# Botón para incrementar el contador.
btn_count_up = tk.Button(button_frame, text="Count Up", command=incrementar, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"), relief="raised", bd=3)
btn_count_up.grid(row=0, column=0, padx=10)  # Coloca el botón en la primera columna del frame de botones.

# Botón para decrementar el contador.
btn_count_down = tk.Button(button_frame, text="Count Down", command=decrementar, bg="#F44336", fg="white", font=("Helvetica", 12, "bold"), relief="raised", bd=3)
btn_count_down.grid(row=0, column=1, padx=10)  # Coloca el botón en la segunda columna del frame de botones.

# Botón para resetear el contador.
btn_reset = tk.Button(button_frame, text="Reset", command=resetear, bg="#FFC107", fg="black", font=("Helvetica", 12, "bold"), relief="raised", bd=3)
btn_reset.grid(row=0, column=2, padx=10)  # Coloca el botón en la tercera columna del frame de botones.

# Inicia el bucle principal de tkinter.
root.mainloop()
