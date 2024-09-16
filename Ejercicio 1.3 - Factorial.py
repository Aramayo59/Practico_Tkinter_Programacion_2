import tkinter as tk  # Biblioteca para la interfaz gráfica
import math  # Biblioteca matemática para el cálculo de factoriales

# Función para calcular el factorial de un número ingresado
def calcular_factorial():
    try:
        n = int(n_var.get())  # Obtiene el valor de la variable n_var como entero
        n_factorial = math.factorial(n)  # Calcula el factorial usando la función math.factorial
        factorial_var.set(f"Factorial({n}) = {n_factorial}")  # Muestra el resultado en la etiqueta
    except ValueError:
        factorial_var.set("Ingrese un número válido.")  # Muestra un error si la entrada no es válida

# Función para incrementar el número y calcular el factorial
def siguiente_numero():
    try:
        n = int(n_var.get())  # Obtiene el valor actual de la variable n_var
        n_var.set(n + 1)  # Incrementa en 1 el valor actual
        calcular_factorial()  # Calcula el factorial del nuevo valor
    except ValueError:
        n_var.set(1)  # Si hay un error, establece el valor de n_var en 1

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Factoriales")  # Título de la ventana

root.configure(bg='#87CEEB')  # Configura el fondo de la ventana con un color azul claro
font_style = ('Helvetica', 12)  # Estilo de fuente predeterminado para los widgets

# Variables tkinter para almacenar el número y el resultado del factorial
n_var = tk.IntVar()
factorial_var = tk.StringVar()

n_var.set(1)  # Inicializa el valor de n_var en 1
factorial_var.set("Factorial(1) = 1")  # Inicializa el texto del factorial con el valor para 1

# Crear un frame para organizar los widgets
frame = tk.Frame(root, bg='#87CEEB', pady=20)  # Fondo azul claro con padding vertical
frame.pack(padx=20, pady=20)  # Empaqueta el frame con un padding adicional alrededor

# Etiqueta para mostrar el texto "Número (n):"
tk.Label(frame, text="Número (n):", font=font_style, bg='#87CEEB', fg='black').grid(row=0, column=0, padx=10, pady=10, sticky='e')

# Campo de entrada para el número (n)
n_entry = tk.Entry(frame, textvariable=n_var, width=10, font=font_style, bg='white', fg='black')
n_entry.grid(row=0, column=1, padx=10, pady=10)

# Etiqueta para mostrar el resultado del factorial
tk.Label(frame, textvariable=factorial_var, font=font_style, bg='#87CEEB', fg='black').grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Frame para los botones
button_frame = tk.Frame(frame, bg='#87CEEB')
button_frame.grid(row=2, column=0, columnspan=2, pady=10)

# Botón para calcular el factorial del número actual
tk.Button(button_frame, text="Calcular Factorial", command=calcular_factorial, font=font_style, bg='#FFA500', fg='black').pack(side='left', padx=10)

# Botón para incrementar el número y calcular el factorial del siguiente número
tk.Button(button_frame, text="Siguiente Número", command=siguiente_numero, font=font_style, bg='#FFA500', fg='black').pack(side='left', padx=10)

# Inicia el bucle principal para mostrar la ventana y esperar eventos
root.mainloop()
