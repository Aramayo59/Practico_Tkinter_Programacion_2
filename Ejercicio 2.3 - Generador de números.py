import tkinter as tk
import random

def generar_numero():
    try:
        num1 = int(spinbox1.get())
        num2 = int(spinbox2.get())
        if num1 > num2:
            numero_var.set("Error: Num1 > Num2")
        else:
            numero_generado = random.randint(num1, num2)
            numero_var.set(numero_generado)
    except ValueError:
        numero_var.set("Error: Valor inválido")

root = tk.Tk()
root.title("Generador de Números")

root.geometry("400x550")
root.minsize(300, 250)

bg_color = "#e8f5e9"  # Verde claro
entry_bg = "#c8e6c9"  # Verde más oscuro
button_bg = "#43a047"  # Verde medio
button_fg = "#ffffff"  # Blanco
spinbox_bg = "#c8e6c9"  # Verde más oscuro
spinbox_fg = "#000000"  # Negro
label_fg = "#fbc02d"  # Amarillo dorado

root.configure(bg=bg_color)

numero_var = tk.StringVar()

tk.Label(root, text="Número 1", font=("Arial", 12), bg=bg_color, fg=label_fg).pack(pady=(10, 5))
spinbox1 = tk.Spinbox(root, from_=0, to=1000, bg=spinbox_bg, fg=spinbox_fg, font=("Arial", 12))
spinbox1.pack(pady=(0, 10))
tk.Label(root, text="Número 2", font=("Arial", 12), bg=bg_color, fg=label_fg).pack(pady=(10, 5))
spinbox2 = tk.Spinbox(root, from_=0, to=1000, bg=spinbox_bg, fg=spinbox_fg, font=("Arial", 12))
spinbox2.pack(pady=(0, 10))
tk.Label(root, text="Número Generado", font=("Arial", 12), bg=bg_color, fg=label_fg).pack(pady=(10, 5))
tk.Entry(root, textvariable=numero_var, state="readonly", font=("Arial", 12), bg=entry_bg, fg="#000000").pack(pady=(0, 10))
tk.Button(root, text="Generar", command=generar_numero, font=("Arial", 12), bg=button_bg, fg=button_fg).pack(pady=(10, 10))

root.mainloop()
