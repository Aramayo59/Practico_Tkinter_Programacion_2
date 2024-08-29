import tkinter as tk

def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 == 0:
        return "Error: Div/0"
    return num1 / num2

def modulo(num1, num2):
    return num1 % num2

operaciones = {
    "+": sumar,
    "-": restar,
    "*": multiplicar,
    "/": dividir,
    "%": modulo
}

def calcular(operacion):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        resultado = operaciones[operacion](num1, num2)
        
        if isinstance(resultado, float):
            if resultado.is_integer():
                resultado = int(resultado)
            else:
                resultado = f"{resultado:.2f}"
        result_var.set(resultado)
    except ValueError:
        result_var.set("Error")

def reset():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_var.set("")

def on_enter(event):
    event.widget.config(bg="#00509e") 

def on_leave(event):
    event.widget.config(bg=btn_color)  

root = tk.Tk()
root.title("Calculadora")

root.configure(bg="#2e2e2e")


root.geometry("600x300")
root.resizable(False, False)

tk.Label(root, text="Primer número", bg="#2e2e2e", fg="#ffffff", font=("Arial", 12)).grid(row=0, column=0, padx=15, pady=10, sticky="w")
entry1 = tk.Entry(root, font=("Arial", 12), bg="#ffffff", fg="#000000", width=20)
entry1.grid(row=0, column=1, padx=15, pady=10)

tk.Label(root, text="Segundo número", bg="#2e2e2e", fg="#ffffff", font=("Arial", 12)).grid(row=1, column=0, padx=15, pady=10, sticky="w")
entry2 = tk.Entry(root, font=("Arial", 12), bg="#ffffff", fg="#000000", width=20)
entry2.grid(row=1, column=1, padx=15, pady=10)

tk.Label(root, text="Resultado", bg="#2e2e2e", fg="#ffffff", font=("Arial", 12)).grid(row=2, column=0, padx=15, pady=10, sticky="w")
result_var = tk.StringVar()
tk.Entry(root, textvariable=result_var, state="readonly", font=("Arial", 12), bg="#ffffff", fg="#000000", width=20).grid(row=2, column=1, padx=15, pady=10)

btn_color = "#003366"
btn_fg_color = "#ffffff"
btn_width = 10
btn_height = 2

button_options = {
    "+": (3, 0),
    "-": (3, 1),
    "*": (3, 2),
    "/": (4, 0),
    "%": (4, 1),
    "RESET": (4, 2)
}

for text, pos in button_options.items():
    color = btn_color if text != "RESET" else "#ff4d4d"
    btn = tk.Button(root, text=text, command=lambda t=text: calcular(t) if t != "RESET" else reset(), 
                    bg=color, fg=btn_fg_color, font=("Arial", 14, "bold"), width=btn_width, height=btn_height, relief="raised", bd=2)
    btn.grid(row=pos[0], column=pos[1], padx=10, pady=10, sticky="nsew")
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)


for i in range(5):
    root.grid_columnconfigure(i, weight=1)
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
