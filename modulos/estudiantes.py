import sqlite3

# Crear estudiante
def crear_estudiante(nombre, email, edad, curso, telefono, direccion):
    conexion = sqlite3.connect("modulos/base_datos/database.db")
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO estudiantes (nombre, email, edad, curso, telefono, direccion)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (nombre, email, edad, curso, telefono, direccion))
    conexion.commit()
    conexion.close()

# Leer estudiantes
def ver_estudiantes():
    conexion = sqlite3.connect("modulos/base_datos/database.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM estudiantes")
    estudiantes = cursor.fetchall()
    conexion.close()
    return estudiantes

# Eliminar estudiante
def eliminar_estudiante(id_estudiante):
    conexion = sqlite3.connect("modulos/base_datos/database.db")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM estudiantes WHERE id = ?", (id_estudiante,))
    conexion.commit()
    conexion.close()

# Actualizar estudiante
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

