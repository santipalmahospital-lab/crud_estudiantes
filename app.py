import tkinter as tk
from modulos.estudiantes import crear_estudiante, leer_estudiantes, eliminar_estudiante, actualizar_estudiante

# Crear ventana principal
root = tk.Tk()
root.title("Gestión de Estudiantes")

# Campos de entrada
tk.Label(root, text="Nombre").grid(row=0, column=0)
nombre = tk.Entry(root)
nombre.grid(row=0, column=1)

tk.Label(root, text="Email").grid(row=1, column=0)
email = tk.Entry(root)
email.grid(row=1, column=1)

tk.Label(root, text="Edad").grid(row=2, column=0)
edad = tk.Entry(root)
edad.grid(row=2, column=1)

tk.Label(root, text="Curso").grid(row=3, column=0)
curso = tk.Entry(root)
curso.grid(row=3, column=1)

# Función para registrar
def registrar():
    crear_estudiante(nombre.get(), email.get(), edad.get(), curso.get())
    print("Estudiante registrado")

tk.Button(root, text="Registrar", command=registrar).grid(row=4, column=0, columnspan=2)

# Función para mostrar estudiantes
def mostrar_estudiantes():
    estudiantes = leer_estudiantes()
    ventana_lista = tk.Toplevel(root)
    ventana_lista.title("Lista de Estudiantes")

    tk.Label(ventana_lista, text="ID | Nombre | Email | Edad | Curso", font=("Arial", 10, "bold")).pack()

    for e in estudiantes:
        texto = f"{e[0]} | {e[1]} | {e[2]} | {e[3]} | {e[4]}"
        tk.Label(ventana_lista, text=texto).pack()

tk.Button(root, text="Ver Estudiantes", command=mostrar_estudiantes).grid(row=5, column=0, columnspan=2)

# Campo y botón para eliminar
tk.Label(root, text="ID a eliminar").grid(row=6, column=0)
id_eliminar = tk.Entry(root)
id_eliminar.grid(row=6, column=1)

def eliminar():
    eliminar_estudiante(int(id_eliminar.get()))
    print("Estudiante eliminado")

tk.Button(root, text="Eliminar Estudiante", command=eliminar).grid(row=7, column=0, columnspan=2)

# Campo y botón para actualizar
tk.Label(root, text="ID a actualizar").grid(row=8, column=0)
id_actualizar = tk.Entry(root)
id_actualizar.grid(row=8, column=1)

def actualizar():
    actualizar_estudiante(
        int(id_actualizar.get()),
        nombre.get(),
        email.get(),
        edad.get(),
        curso.get()
    )
    print("Estudiante actualizado")

tk.Button(root, text="Actualizar Estudiante", command=actualizar).grid(row=9, column=0, columnspan=2)

# Mantener la ventana abierta
root.mainloop()
# Campo y botón para eliminar
tk.Label(root, text="ID a eliminar").grid(row=6, column=0)
id_eliminar = tk.Entry(root)
id_eliminar.grid(row=6, column=1)

def eliminar():
    eliminar_estudiante(int(id_eliminar.get()))
    print("Estudiante eliminado")

tk.Button(root, text="Eliminar Estudiante", command=eliminar).grid(row=7, column=0, columnspan=2)

# Campo y botón para actualizar
tk.Label(root, text="ID a actualizar").grid(row=8, column=0)
id_actualizar = tk.Entry(root)
id_actualizar.grid(row=8, column=1)

def actualizar():
    actualizar_estudiante(
        int(id_actualizar.get()),
        nombre.get(),
        email.get(),
        edad.get(),
        curso.get()
    )
    print("Estudiante actualizado")

tk.Button(root, text="Actualizar Estudiante", command=actualizar).grid(row=9, column=0, columnspan=2)

# Mantener la ventana abierta
root.mainloop()

import tkinter as tk
from modulos.estudiantes import crear_estudiante, ver_estudiantes

# Ventana principal
root = tk.Tk()
root.title("Gestión de Estudiantes")

# Campos de entrada
tk.Label(root, text="Nombre").grid(row=0, column=0)
nombre = tk.Entry(root)
nombre.grid(row=0, column=1)

tk.Label(root, text="Email").grid(row=1, column=0)
email = tk.Entry(root)
email.grid(row=1, column=1)

tk.Label(root, text="Edad").grid(row=2, column=0)
edad = tk.Entry(root)
edad.grid(row=2, column=1)

tk.Label(root, text="Curso").grid(row=3, column=0)
curso = tk.Entry(root)
curso.grid(row=3, column=1)

tk.Label(root, text="Teléfono").grid(row=4, column=0)
telefono = tk.Entry(root)
telefono.grid(row=4, column=1)

tk.Label(root, text="Dirección").grid(row=5, column=0)
direccion = tk.Entry(root)
direccion.grid(row=5, column=1)

# Funciones de botones
def registrar():
    crear_estudiante(
        nombre.get(),
        email.get(),
        edad.get(),
        curso.get(),
        telefono.get(),
        direccion.get()
    )
    nombre.delete(0, tk.END)
    email.delete(0, tk.END)
    edad.delete(0, tk.END)
    curso.delete(0, tk.END)
    telefono.delete(0, tk.END)
    direccion.delete(0, tk.END)

def mostrar():
    estudiantes = ver_estudiantes()
    for est in estudiantes:
        print(est)

# Botones
tk.Button(root, text="Registrar", command=registrar).grid(row=6, column=0)
tk.Button(root, text="Ver Estudiantes", command=mostrar).grid(row=6, column=1)

root.mainloop()
