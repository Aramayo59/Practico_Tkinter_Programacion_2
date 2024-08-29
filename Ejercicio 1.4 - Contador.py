import tkinter as tk

def incrementar():
    """Incrementa el valor del contador en 1."""
    contador.set(contador.get() + 1)

def decrementar():
    """Decrementa el valor del contador en 1."""
    contador.set(contador.get() - 1)

def resetear():
    """Reinicia el valor del contador a 0."""
    contador.set(0)


root = tk.Tk()
root.title("Contador")
root.geometry("700x400") 
root.configure(bg="#f0f8ff")  


root.resizable(False, False)

contador = tk.IntVar()
contador.set(0)


main_frame = tk.Frame(root, bg="#f0f8ff", padx=20, pady=20)
main_frame.pack(expand=True, fill=tk.BOTH)


label = tk.Label(main_frame, text="Contador", bg="#f0f8ff", font=("Helvetica", 20, "bold"))
label.grid(row=0, column=0, columnspan=2, pady=10)


entrada = tk.Entry(main_frame, textvariable=contador, state="readonly", font=("Helvetica", 40, "bold"), bg="white", bd=2, relief="solid")
entrada.grid(row=1, column=0, columnspan=2, pady=10, padx=10)


button_frame = tk.Frame(main_frame, bg="#f0f8ff")
button_frame.grid(row=2, column=0, columnspan=2, pady=10)

btn_count_up = tk.Button(button_frame, text="Count Up", command=incrementar, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"), relief="raised", bd=3)
btn_count_up.grid(row=0, column=0, padx=10)

btn_count_down = tk.Button(button_frame, text="Count Down", command=decrementar, bg="#F44336", fg="white", font=("Helvetica", 12, "bold"), relief="raised", bd=3)
btn_count_down.grid(row=0, column=1, padx=10)

btn_reset = tk.Button(button_frame, text="Reset", command=resetear, bg="#FFC107", fg="black", font=("Helvetica", 12, "bold"), relief="raised", bd=3)
btn_reset.grid(row=0, column=2, padx=10)


root.mainloop()
