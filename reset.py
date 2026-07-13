import sqlite3

conexion = sqlite3.connect("modulos/base_datos/database.db")
cursor = conexion.cursor()

cursor.execute("""
    DELETE FROM estudiantes
    WHERE id NOT IN (
        SELECT MIN(id)
        FROM estudiantes
        GROUP BY email
    )
""")

conexion.commit()
conexion.close()
print("✅ Duplicados eliminados.")
