import tkinter as tk

def añadir_pelicula():
    pelicula = pelicula_var.get()
    if pelicula:
        listbox.insert(tk.END, pelicula)
        pelicula_var.set("")

root = tk.Tk()
root.title("Películas")

root.geometry("550x450")
root.minsize(350, 350)

bg_color = "#2e2e2e"  # Gris oscuro
entry_bg = "#424242"  # Gris oscuro
button_bg = "#607d8b"  # Azul grisáceo
button_fg = "#ffffff"  # Blanco
listbox_bg = "#37474f"  # Gris azulado oscuro
listbox_fg = "#ffffff"  # Blanco
label_fg = "#b0bec5"  # Gris claro

root.configure(bg=bg_color)

pelicula_var = tk.StringVar()

tk.Label(root, text="Escribe el título de una película", font=("Arial", 12), bg=bg_color, fg=label_fg).pack(pady=(10, 5))
tk.Entry(root, textvariable=pelicula_var, font=("Arial", 12), bg=entry_bg, fg="#ffffff", width=30).pack(pady=(0, 10))
tk.Label(root, text="Películas", font=("Arial", 12), bg=bg_color, fg=label_fg).pack(pady=(10, 5))

listbox = tk.Listbox(root, font=("Arial", 12), width=40, height=10, bg=listbox_bg, fg=listbox_fg, borderwidth=2, relief="solid")
listbox.pack(pady=(0, 10))

tk.Button(root, text="Añadir", command=añadir_pelicula, font=("Arial", 12), bg=button_bg, fg=button_fg).pack(pady=(10, 10))

root.mainloop()
