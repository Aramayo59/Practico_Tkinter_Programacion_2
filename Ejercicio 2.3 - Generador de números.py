import tkinter as tk  # Importa tkinter para la interfaz gráfica.
import random  # Importa la biblioteca random para generar números aleatorios.

# Función que genera un número aleatorio entre dos valores.
def generar_numero():
    try:
        # Obtiene los valores de los spinboxes y los convierte en enteros.
        num1 = int(spinbox1.get())
        num2 = int(spinbox2.get())

        # Verifica si el primer número es mayor que el segundo.
        if num1 > num2:
            numero_var.set("Error: Num1 > Num2")  # Error si num1 es mayor que num2.
        else:
            numero_generado = random.randint(num1, num2)  # Genera un número aleatorio entre num1 y num2.
            numero_var.set(numero_generado)  # Muestra el número generado.
    except ValueError:
        # Maneja el caso en que los valores ingresados no son válidos.
        numero_var.set("Error: Valor inválido")

# Crear la ventana principal.
root = tk.Tk()
root.title("Generador de Números")  # Título de la ventana.

# Configura el tamaño de la ventana.
root.geometry("400x550")  # Tamaño inicial de la ventana.
root.minsize(300, 250)  # Tamaño mínimo de la ventana.

# Colores utilizados en la interfaz.
bg_color = "#e8f5e9"  # Verde claro.
entry_bg = "#c8e6c9"  # Verde más oscuro para los campos de entrada.
button_bg = "#43a047"  # Verde medio para los botones.
button_fg = "#ffffff"  # Texto blanco para los botones.
spinbox_bg = "#c8e6c9"  # Verde más oscuro para los spinboxes.
spinbox_fg = "#000000"  # Texto negro en los spinboxes.
label_fg = "#fbc02d"  # Color amarillo dorado para las etiquetas.

# Configura el color de fondo de la ventana.
root.configure(bg=bg_color)

# Variable que almacena el resultado del número generado.
numero_var = tk.StringVar()

# Etiqueta y Spinbox para el primer número.
tk.Label(root, text="Número 1", font=("Arial", 12), bg=bg_color, fg=label_fg).pack(pady=(10, 5))
spinbox1 = tk.Spinbox(root, from_=0, to=1000, bg=spinbox_bg, fg=spinbox_fg, font=("Arial", 12))  # Spinbox con rango de 0 a 1000.
spinbox1.pack(pady=(0, 10))

# Etiqueta y Spinbox para el segundo número.
tk.Label(root, text="Número 2", font=("Arial", 12), bg=bg_color, fg=label_fg).pack(pady=(10, 5))
spinbox2 = tk.Spinbox(root, from_=0, to=1000, bg=spinbox_bg, fg=spinbox_fg, font=("Arial", 12))  # Spinbox con rango de 0 a 1000.
spinbox2.pack(pady=(0, 10))

# Etiqueta y campo de entrada para mostrar el número generado.
tk.Label(root, text="Número Generado", font=("Arial", 12), bg=bg_color, fg=label_fg).pack(pady=(10, 5))
tk.Entry(root, textvariable=numero_var, state="readonly", font=("Arial", 12), bg=entry_bg, fg="#000000").pack(pady=(0, 10))

# Botón para generar el número aleatorio.
tk.Button(root, text="Generar", command=generar_numero, font=("Arial", 12), bg=button_bg, fg=button_fg).pack(pady=(10, 10))

# Inicia el bucle principal de la aplicación.
root.mainloop()
