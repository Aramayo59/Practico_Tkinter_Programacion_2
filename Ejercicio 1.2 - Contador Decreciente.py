import tkinter as tk

def decrementar():
    contador.set(contador.get() - 1)

root = tk.Tk()
root.title("ContDecreciente")
root.geometry("400x250")  
root.configure(bg="#1a1a1a") 


root.resizable(False, False)

contador = tk.IntVar()
contador.set(88)


frame = tk.Frame(root, bg="#1a1a1a")
frame.place(relx=0.5, rely=0.5, anchor="center")


tk.Label(frame, text="Contador", font=("Arial", 14), bg="#1a1a1a", fg="#cc0000").pack(pady=5)

tk.Entry(frame, textvariable=contador, state="readonly", font=("Arial", 14), justify="center", bg="#cc0000", fg="black").pack(pady=5)  # Fondo rojo, texto negro


tk.Button(frame, text="-", font=("Arial", 14), command=decrementar, bg="#cc0000", fg="white", activebackground="#b30000", activeforeground="white").pack(pady=10)

root.mainloop()
