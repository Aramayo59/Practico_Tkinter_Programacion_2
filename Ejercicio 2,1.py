import tkinter as tk  # Importa la biblioteca tkinter para crear la interfaz gráfica.

# Funciones para cada operación matemática.
def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 == 0:
        return "Error: Div/0"  # Previene la división por cero.
    return num1 / num2

def modulo(num1, num2):
    return num1 % num2

# Diccionario que asocia cada operador con su función correspondiente.
operaciones = {
    "+": sumar,
    "-": restar,
    "*": multiplicar,
    "/": dividir,
    "%": modulo
}

# Función que realiza el cálculo según la operación seleccionada.
def calcular(operacion):
    try:
        num1 = float(entry1.get())  # Obtiene el primer número desde la entrada de texto.
        num2 = float(entry2.get())  # Obtiene el segundo número desde la entrada de texto.
        resultado = operaciones[operacion](num1, num2)  # Llama a la función correspondiente según la operación.
        
        if isinstance(resultado, float):  # Si el resultado es un número decimal:
            if resultado.is_integer():  # Si es un entero (por ejemplo, 4.0), lo convierte a entero.
                resultado = int(resultado)
            else:
                resultado = f"{resultado:.2f}"  # Si no, lo muestra con 2 decimales.
        result_var.set(resultado)  # Establece el resultado en la variable vinculada al cuadro de texto.
    except ValueError:
        result_var.set("Error")  # Muestra un error si los valores ingresados no son válidos.

# Función para resetear las entradas y el resultado.
def reset():
    entry1.delete(0, tk.END)  # Borra el contenido del primer campo.
    entry2.delete(0, tk.END)  # Borra el contenido del segundo campo.
    result_var.set("")  # Resetea el resultado.

# Funciones para cambiar el color de los botones al pasar el cursor.
def on_enter(event):
    event.widget.config(bg="#00509e")  # Cambia el color del fondo del botón al azul más oscuro.

def on_leave(event):
    event.widget.config(bg=btn_color)  # Restablece el color original cuando el cursor sale del botón.

# Crear la ventana principal.
root = tk.Tk()
root.title("Calculadora")  # Título de la ventana.
root.configure(bg="#2e2e2e")  # Fondo gris oscuro para la ventana.

root.geometry("600x300")  # Tamaño de la ventana.
root.resizable(False, False)  # Evita que la ventana cambie de tamaño.

# Etiqueta y campo de entrada para el primer número.
tk.Label(root, text="Primer número", bg="#2e2e2e", fg="#ffffff", font=("Arial", 12)).grid(row=0, column=0, padx=15, pady=10, sticky="w")
entry1 = tk.Entry(root, font=("Arial", 12), bg="#ffffff", fg="#000000", width=20)
entry1.grid(row=0, column=1, padx=15, pady=10)

# Etiqueta y campo de entrada para el segundo número.
tk.Label(root, text="Segundo número", bg="#2e2e2e", fg="#ffffff", font=("Arial", 12)).grid(row=1, column=0, padx=15, pady=10, sticky="w")
entry2 = tk.Entry(root, font=("Arial", 12), bg="#ffffff", fg="#000000", width=20)
entry2.grid(row=1, column=1, padx=15, pady=10)

# Etiqueta y campo de entrada para mostrar el resultado.
tk.Label(root, text="Resultado", bg="#2e2e2e", fg="#ffffff", font=("Arial", 12)).grid(row=2, column=0, padx=15, pady=10, sticky="w")
result_var = tk.StringVar()  # Variable que almacena el resultado.
tk.Entry(root, textvariable=result_var, state="readonly", font=("Arial", 12), bg="#ffffff", fg="#000000", width=20).grid(row=2, column=1, padx=15, pady=10)

# Configuración de los botones para las operaciones.
btn_color = "#003366"  # Color de fondo por defecto de los botones.
btn_fg_color = "#ffffff"  # Color del texto de los botones.
btn_width = 10  # Ancho de los botones.
btn_height = 2  # Alto de los botones.

# Diccionario con la configuración de posición de los botones.
button_options = {
    "+": (3, 0),
    "-": (3, 1),
    "*": (3, 2),
    "/": (4, 0),
    "%": (4, 1),
    "RESET": (4, 2)
}

# Crear y configurar cada botón en su posición correspondiente.
for text, pos in button_options.items():
    color = btn_color if text != "RESET" else "#ff4d4d"  # El botón "RESET" tiene un color rojo especial.
    btn = tk.Button(root, text=text, command=lambda t=text: calcular(t) if t != "RESET" else reset(), 
                    bg=color, fg=btn_fg_color, font=("Arial", 14, "bold"), width=btn_width, height=btn_height, relief="raised", bd=2)
    btn.grid(row=pos[0], column=pos[1], padx=10, pady=10, sticky="nsew")  # Coloca el botón en la posición correspondiente.
    btn.bind("<Enter>", on_enter)  # Vincula la acción de cambiar el color cuando el cursor pasa sobre el botón.
    btn.bind("<Leave>", on_leave)  # Vincula la acción de restablecer el color cuando el cursor sale del botón.

# Configura las columnas y filas para que el diseño sea responsivo dentro de la ventana.
for i in range(5):
    root.grid_columnconfigure(i, weight=1)
    root.grid_rowconfigure(i, weight=1)

# Inicia el bucle principal de la aplicación.
root.mainloop()
