import sqlite3


def conectar():
    return sqlite3.connect("modulos/base_datos/database.db")


def crear_estudiante(nombre, email, edad, curso, telefono, direccion):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM estudiantes WHERE email = ?", (email,))
    existente = cursor.fetchone()

    if existente:
        print("⚠️ El estudiante ya está registrado.")
    else:
        cursor.execute("""
            INSERT INTO estudiantes 
            (nombre, email, edad, curso, telefono, direccion)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (nombre, email, edad, curso, telefono, direccion))

        conexion.commit()
        print("✅ Estudiante registrado correctamente.")

    conexion.close()


def ver_estudiantes():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM estudiantes")
    estudiantes = cursor.fetchall()

    conexion.close()

    return estudiantes


def eliminar_estudiante(id_estudiante):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        "DELETE FROM estudiantes WHERE id = ?",
        (id_estudiante,)
    )

    conexion.commit()
    conexion.close()

    print("✅ Estudiante eliminado correctamente.")


def actualizar_estudiante(id_estudiante, nombre, email, edad, curso, telefono, direccion):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE estudiantes
        SET nombre = ?,
            email = ?,
            edad = ?,
            curso = ?,
            telefono = ?,
            direccion = ?
        WHERE id = ?
    """, (
        nombre,
        email,
        edad,
        curso,
        telefono,
        direccion,
        id_estudiante
    ))

    conexion.commit()
    conexion.close()

    print("✅ Estudiante actualizado correctamente.")
    
