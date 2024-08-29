import tkinter as tk

def calcular():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operacion = operacion_var.get()
        if operacion == "Sumar":
            resultado = num1 + num2
        elif operacion == "Restar":
            resultado = num1 - num2
        elif operacion == "Multiplicar":
            resultado = num1 * num2
        elif operacion == "Dividir":
            if num2 == 0:
                resultado = "Error: Div/0"
            else:
                resultado = num1 / num2
        # Eliminar decimales innecesarios
        if isinstance(resultado, float) and resultado.is_integer():
            resultado = int(resultado)
        result_var.set(resultado)
    except ValueError:
        result_var.set("Error")

root = tk.Tk()
root.title("Calculadora 2")

root.geometry("600x550")
root.minsize(300, 300)

bg_color = "#b71c1c"  # Rojo más oscuro
entry_bg = "#ffffff"  # Blanco
text_color = "#000000"  # Negro

root.configure(bg=bg_color)

entry1 = tk.Entry(root, font=("Arial", 12), bg=entry_bg, fg=text_color)
entry1.pack(pady=(10, 5), padx=10, fill=tk.X)
entry2 = tk.Entry(root, font=("Arial", 12), bg=entry_bg, fg=text_color)
entry2.pack(pady=(5, 10), padx=10, fill=tk.X)

result_var = tk.StringVar()
tk.Label(root, text="Resultado", font=("Arial", 12), bg=bg_color, fg=text_color).pack(pady=(10, 5))
tk.Entry(root, textvariable=result_var, state="readonly", font=("Arial", 12), bg=entry_bg, fg=text_color).pack(pady=(5, 10), padx=10, fill=tk.X)

tk.Label(root, text="Operaciones", font=("Arial", 12), bg=bg_color, fg=text_color).pack(pady=(10, 5))

operacion_var = tk.StringVar(value="Sumar")
tk.Radiobutton(root, text="Sumar", variable=operacion_var, value="Sumar", bg=bg_color, fg=text_color, font=("Arial", 12)).pack(pady=5, padx=10, anchor=tk.W)
tk.Radiobutton(root, text="Restar", variable=operacion_var, value="Restar", bg=bg_color, fg=text_color, font=("Arial", 12)).pack(pady=5, padx=10, anchor=tk.W)
tk.Radiobutton(root, text="Multiplicar", variable=operacion_var, value="Multiplicar", bg=bg_color, fg=text_color, font=("Arial", 12)).pack(pady=5, padx=10, anchor=tk.W)
tk.Radiobutton(root, text="Dividir", variable=operacion_var, value="Dividir", bg=bg_color, fg=text_color, font=("Arial", 12)).pack(pady=5, padx=10, anchor=tk.W)

tk.Button(root, text="Calcular", command=calcular, font=("Arial", 12), bg="#ffffff", fg=text_color).pack(pady=20, padx=10)

root.mainloop()
