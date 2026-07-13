import sqlite3

def crear_estudiante(nombre, email, edad, curso, telefono, direccion):
    conexion = sqlite3.connect("modulos/base_datos/database.db")
    cursor = conexion.cursor()

    # Verificar si el estudiante ya existe por email
    cursor.execute("SELECT * FROM estudiantes WHERE email = ?", (email,))
    existente = cursor.fetchone()

    if existente:
        print("⚠️ El estudiante ya está registrado.")
    else:
        cursor.execute("""
            INSERT INTO estudiantes (nombre, email, edad, curso, telefono, direccion)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (nombre, email, edad, curso, telefono, direccion))
        conexion.commit()
        print("✅ Estudiante registrado correctamente.")

    conexion.close()
