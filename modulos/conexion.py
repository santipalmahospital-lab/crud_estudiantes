import sqlite3

def crear_base_datos():
    conn = sqlite3.connect("modulos/base_datos/database.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS estudiantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT NOT NULL,
            edad INTEGER NOT NULL,
            curso TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Ejecutar la función automáticamente al correr el archivo
if __name__ == "__main__":
    crear_base_datos()

