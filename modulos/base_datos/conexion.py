import sqlite3

def crear_base_datos():
    # Conexión a la base de datos (se crea si no existe)
    conexion = sqlite3.connect("modulos/base_datos/database.db")
    cursor = conexion.cursor()

    # Crear tabla estudiantes con todas las columnas necesarias
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS estudiantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT NOT NULL,
            edad INTEGER NOT NULL,
            curso TEXT NOT NULL,
            telefono TEXT,
            direccion TEXT
        )
    """)

    conexion.commit()
    conexion.close()

# Ejecutar directamente si corres este archivo
if __name__ == "__main__":
    crear_base_datos()
    print("Base de datos y tabla 'estudiantes' creadas correctamente.")



