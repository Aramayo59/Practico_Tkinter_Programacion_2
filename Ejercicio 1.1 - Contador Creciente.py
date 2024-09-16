import tkinter as tk #Se importa la biblioteca tkinter, que es una biblioteca estándar de Python para crear interfaces gráficas.

def incrementar():           
    try: 
        contador.set(contador.get() + 1)
    except Exception as e:
        print("Error al incrementar el contador")   
    #Esta función se ejecuta cuando el usuario hace clic en el botón "+". Dentro de un bloque try, toma el valor actual del contador (contador.get()),
    #lo incrementa en 1 y lo actualiza usando contador.set(). Si ocurre algún error, lo captura y muestra un mensaje de error.
        
#Crear la ventana principal:
root = tk.Tk()   #crea la ventana principal de la aplicación
root.title("Contador Creciente") # Establece el titulo de la aplicacion
root.geometry("500x300")  #Define el tamaño de la ventana
root.configure(bg="#1a1a1a")  # Establese el color de fondo de la pantalla en un tono oscuro
root.resizable(False, False) #Impide que se pueda cambiar el tamaño e la pantalla

#Variable de contador
contador = tk.IntVar()#contador es una variable de tipo IntVar() de tkinter que contiene el valor del contador. Se inicializa en 0 con contador.set(0).
contador.set(0)

#Crear un Frame:
frame = tk.Frame(root, bg="#1a1a1a")
frame.place(relx=0.5, rely=0.5, anchor="center")
#Se crea un contenedor (frame) para los widgets. Se coloca en el centro de la ventana usando relx=0.5 y rely=0.5, que indican la posición relativa.

#Etiqueta del contador:
tk.Label(frame, text="Contador", font=("Arial", 14), bg="#1a1a1a", fg="#cc6600").pack(pady=5)
#Se crea una etiqueta que muestra la palabra "Contador". Se personaliza con una fuente Arial de tamaño 14, fondo oscuro (#1a1a1a) y texto en color naranja (#cc6600).
#El método pack(pady=5) coloca la etiqueta en el contenedor con un margen vertical de 5 píxeles.

#Campo de entrada de solo lectura
tk.Entry(frame, textvariable=contador, state="readonly", font=("Arial", 14), justify="center", bg="#333333", fg="#cc6600").pack(pady=5)
#Un campo de entrada muestra el valor actual del contador. Está vinculado a la variable contador y tiene un estado de solo lectura (state="readonly").
#Su apariencia está personalizada con una fuente, colores de fondo y texto.

#Botón para incrementar:
tk.Button(frame, text="+", font=("Arial", 14), command=incrementar, bg="#cc6600", fg="white", activebackground="#b35900", activeforeground="white").pack(pady=10)
#Este botón tiene un texto "+", y al ser presionado ejecuta la función incrementar(). Los colores del botón y su estilo están personalizados.

#Bucle principal:
root.mainloop() #Esto inicia el bucle principal de la ventana, manteniéndola abierta y esperando interacciones del usuario.
