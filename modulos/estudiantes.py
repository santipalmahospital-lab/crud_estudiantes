import sqlite3

# Crear estudiante
def crear_estudiante(nombre, email, edad, curso):
    conn = sqlite3.connect("modulos/base_datos/database.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO estudiantes (nombre, email, edad, curso) VALUES (?, ?, ?, ?)",
        (nombre, email, edad, curso)
    )
    conn.commit()
    conn.close()

# Leer estudiantes
def leer_estudiantes():
    conn = sqlite3.connect("modulos/base_datos/database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM estudiantes")
    datos = cursor.fetchall()
    conn.close()
    return datos

# Eliminar estudiante
def eliminar_estudiante(id_estudiante):
    conn = sqlite3.connect("modulos/base_datos/database.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM estudiantes WHERE id = ?", (id_estudiante,))
    conn.commit()
    conn.close()

# Actualizar estudiante
def actualizar_estudiante(id_estudiante, nombre, email, edad, curso):
    conn = sqlite3.connect("modulos/base_datos/database.db")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE estudiantes SET nombre = ?, email = ?, edad = ?, curso = ? WHERE id = ?",
        (nombre, email, edad, curso, id_estudiante)
    )
    conn.commit()
    conn.close()

import sqlite3

def eliminar_estudiante(id_estudiante):
    conexion = sqlite3.connect("modulos/base_datos/database.db")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM estudiantes WHERE id = ?", (id_estudiante,))
    conexion.commit()
    conexion.close()
