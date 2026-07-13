from modulos.estudiantes import leer_estudiantes

def mostrar_estudiantes():
    estudiantes = leer_estudiantes()
    if estudiantes:
        print("📋 Lista de estudiantes registrados:")
        for e in estudiantes:
            print(f"ID: {e[0]} | Nombre: {e[1]} | Email: {e[2]} | Edad: {e[3]} | Curso: {e[4]}")
    else:
        print("⚠️ No hay estudiantes registrados.")

if __name__ == "__main__":
    mostrar_estudiantes()
