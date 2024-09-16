import tkinter as tk  # Importa la biblioteca tkinter para crear interfaces gráficas

# Función que realiza las operaciones aritméticas
def calcular():
    try:
        # Obtiene los valores de los campos de entrada y los convierte a números
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        # Obtiene el tipo de operación seleccionada
        operacion = operacion_var.get()

        # Realiza la operación según lo seleccionado
        if operacion == "Sumar":
            resultado = num1 + num2
        elif operacion == "Restar":
            resultado = num1 - num2
        elif operacion == "Multiplicar":
            resultado = num1 * num2
        elif operacion == "Dividir":
            if num2 == 0:  # Maneja la división por cero
                resultado = "Error: Div/0"
            else:
                resultado = num1 / num2

        # Si el resultado es un número entero, elimina los decimales innecesarios
        if isinstance(resultado, float) and resultado.is_integer():
            resultado = int(resultado)

        # Muestra el resultado en la interfaz
        result_var.set(resultado)

    except ValueError:
        # Muestra un mensaje de error si la entrada no es válida
        result_var.set("Error")

# Crea la ventana principal de la aplicación
root = tk.Tk()
root.title("Calculadora 2")  # Título de la ventana

# Configuración del tamaño de la ventana
root.geometry("600x550")
root.minsize(300, 300)  # Tamaño mínimo de la ventana

# Colores para la interfaz
bg_color = "#b71c1c"  # Rojo oscuro para el fondo
entry_bg = "#ffffff"  # Blanco para los campos de entrada
text_color = "#000000"  # Negro para el texto

# Configura el color de fondo de la ventana
root.configure(bg=bg_color)

# Campos de entrada para los dos números
entry1 = tk.Entry(root, font=("Arial", 12), bg=entry_bg, fg=text_color)
entry1.pack(pady=(10, 5), padx=10, fill=tk.X)  # Ajusta el diseño y coloca el campo en la ventana
entry2 = tk.Entry(root, font=("Arial", 12), bg=entry_bg, fg=text_color)
entry2.pack(pady=(5, 10), padx=10, fill=tk.X)

# Variable para mostrar el resultado
result_var = tk.StringVar()

# Etiqueta para el resultado
tk.Label(root, text="Resultado", font=("Arial", 12), bg=bg_color, fg=text_color).pack(pady=(10, 5))

# Campo de solo lectura para mostrar el resultado
tk.Entry(root, textvariable=result_var, state="readonly", font=("Arial", 12), bg=entry_bg, fg=text_color).pack(pady=(5, 10), padx=10, fill=tk.X)

# Etiqueta para seleccionar la operación
tk.Label(root, text="Operaciones", font=("Arial", 12), bg=bg_color, fg=text_color).pack(pady=(10, 5))

# Variable para seleccionar el tipo de operación con botones de opción
operacion_var = tk.StringVar(value="Sumar")
tk.Radiobutton(root, text="Sumar", variable=operacion_var, value="Sumar", bg=bg_color, fg=text_color, font=("Arial", 12)).pack(pady=5, padx=10, anchor=tk.W)
tk.Radiobutton(root, text="Restar", variable=operacion_var, value="Restar", bg=bg_color, fg=text_color, font=("Arial", 12)).pack(pady=5, padx=10, anchor=tk.W)
tk.Radiobutton(root, text="Multiplicar", variable=operacion_var, value="Multiplicar", bg=bg_color, fg=text_color, font=("Arial", 12)).pack(pady=5, padx=10, anchor=tk.W)
tk.Radiobutton(root, text="Dividir", variable=operacion_var, value="Dividir", bg=bg_color, fg=text_color, font=("Arial", 12)).pack(pady=5, padx=10, anchor=tk.W)

# Botón para realizar el cálculo
tk.Button(root, text="Calcular", command=calcular, font=("Arial", 12), bg="#ffffff", fg=text_color).pack(pady=20, padx=10)

# Inicia el bucle principal de la aplicación (espera eventos)
root.mainloop()
