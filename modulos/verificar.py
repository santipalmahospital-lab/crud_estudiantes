import sqlite3

def mostrar_estudiantes():
    conexion = sqlite3.connect("modulos/base_datos/database.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM estudiantes")
    estudiantes = cursor.fetchall()
    conexion.close()

    print("Listado de estudiantes registrados:\n")
    for est in estudiantes:
        print(f"ID: {est[0]} | Nombre: {est[1]} | Email: {est[2]} | Edad: {est[3]} | Curso: {est[4]} | Teléfono: {est[5]} | Dirección: {est[6]}")

if __name__ == "__main__":
    mostrar_estudiantes()

