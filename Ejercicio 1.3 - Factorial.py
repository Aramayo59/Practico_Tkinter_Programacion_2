import tkinter as tk
import math

def calcular_factorial():
    try:
        n = int(n_var.get())
        n_factorial = math.factorial(n)
        factorial_var.set(f"Factorial({n}) = {n_factorial}")
    except ValueError:
        factorial_var.set("Ingrese un número válido.")

def siguiente_numero():
    try:
        n = int(n_var.get())
        n_var.set(n + 1)
        calcular_factorial()
    except ValueError:
        n_var.set(1)

root = tk.Tk()
root.title("Calculadora de Factoriales")


root.configure(bg='#87CEEB')  
font_style = ('Helvetica', 12)


n_var = tk.IntVar()
factorial_var = tk.StringVar()
n_var.set(1)
factorial_var.set("Factorial(1) = 1") 

frame = tk.Frame(root, bg='#87CEEB', pady=20)
frame.pack(padx=20, pady=20)

tk.Label(frame, text="Número (n):", font=font_style, bg='#87CEEB', fg='black').grid(row=0, column=0, padx=10, pady=10, sticky='e')
n_entry = tk.Entry(frame, textvariable=n_var, width=10, font=font_style, bg='white', fg='black')
n_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(frame, textvariable=factorial_var, font=font_style, bg='#87CEEB', fg='black').grid(row=1, column=0, columnspan=2, padx=10, pady=10)

button_frame = tk.Frame(frame, bg='#87CEEB')
button_frame.grid(row=2, column=0, columnspan=2, pady=10)

tk.Button(button_frame, text="Calcular Factorial", command=calcular_factorial, font=font_style, bg='#FFA500', fg='black').pack(side='left', padx=10)
tk.Button(button_frame, text="Siguiente Número", command=siguiente_numero, font=font_style, bg='#FFA500', fg='black').pack(side='left', padx=10)

root.mainloop()
