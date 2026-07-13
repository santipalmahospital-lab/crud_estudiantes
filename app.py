import sqlite3
from modulos.estudiantes import crear_estudiante, ver_estudiantes, eliminar_estudiante, actualizar_estudiante

def crear_estudiante(nombre, email, edad, curso, telefono, direccion):
    conexion = sqlite3.connect("modulos/base_datos/database.db")
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO estudiantes (nombre, email, edad, curso, telefono, direccion)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (nombre, email, edad, curso, telefono, direccion))
    conexion.commit()
    conexion.close()

def ver_estudiantes():
    conexion = sqlite3.connect("modulos/base_datos/database.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM estudiantes")
    estudiantes = cursor.fetchall()
    conexion.close()
    return estudiantes

def eliminar_estudiante(id_estudiante):
    conexion = sqlite3.connect("modulos/base_datos/database.db")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM estudiantes WHERE id = ?", (id_estudiante,))
    conexion.commit()
    conexion.close()

def actualizar_estudiante(id_estudiante, nombre, email, edad, curso, telefono, direccion):
    conexion = sqlite3.connect("modulos/base_datos/database.db")
    cursor = conexion.cursor()
    cursor.execute("""
        UPDATE estudiantes
        SET nombre = ?, email = ?, edad = ?, curso = ?, telefono = ?, direccion = ?
        WHERE id = ?
    """, (nombre, email, edad, curso, telefono, direccion, id_estudiante))
    conexion.commit()
    conexion.close()
import tkinter as tk
from modulos.estudiantes import crear_estudiante, ver_estudiantes, eliminar_estudiante, actualizar_estudiante

root = tk.Tk()
root.title("Gestión de Estudiantes")

# Campos
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

# Campos para ID
tk.Label(root, text="ID a eliminar").grid(row=6, column=0)
id_eliminar = tk.Entry(root)
id_eliminar.grid(row=6, column=1)

tk.Label(root, text="ID a actualizar").grid(row=7, column=0)
id_actualizar = tk.Entry(root)
id_actualizar.grid(row=7, column=1)

# Funciones
def registrar():
    crear_estudiante(
        nombre.get(),
        email.get(),
        edad.get(),
        curso.get(),
        telefono.get(),
        direccion.get()
    )

def mostrar():
    estudiantes = ver_estudiantes()
    for est in estudiantes:
        print(est)

def eliminar():
    eliminar_estudiante(int(id_eliminar.get()))

def actualizar():
    actualizar_estudiante(
        int(id_actualizar.get()),
        nombre.get(),
        email.get(),
        edad.get(),
        curso.get(),
        telefono.get(),
        direccion.get()
    )

# Botones
tk.Button(root, text="Registrar", command=registrar).grid(row=8, column=0)
tk.Button(root, text="Ver Estudiantes", command=mostrar).grid(row=8, column=1)
tk.Button(root, text="Eliminar", command=eliminar).grid(row=9, column=0)
tk.Button(root, text="Actualizar", command=actualizar).grid(row=9, column=1)

root.mainloop()
