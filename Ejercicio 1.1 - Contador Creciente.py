import tkinter as tk

def incrementar():
    try:
        
        contador.set(contador.get() + 1)
    except Exception as e:
        print("Error al incrementar el contador")

root = tk.Tk()
root.title("Contador Creciente")
root.geometry("500x300")  
root.configure(bg="#1a1a1a")  


root.resizable(False, False)

contador = tk.IntVar()
contador.set(0)


frame = tk.Frame(root, bg="#1a1a1a")
frame.place(relx=0.5, rely=0.5, anchor="center")


tk.Label(frame, text="Contador", font=("Arial", 14), bg="#1a1a1a", fg="#cc6600").pack(pady=5)


tk.Entry(frame, textvariable=contador, state="readonly", font=("Arial", 14), justify="center", bg="#333333", fg="#cc6600").pack(pady=5)


tk.Button(frame, text="+", font=("Arial", 14), command=incrementar, bg="#cc6600", fg="white", activebackground="#b35900", activeforeground="white").pack(pady=10)

root.mainloop()
