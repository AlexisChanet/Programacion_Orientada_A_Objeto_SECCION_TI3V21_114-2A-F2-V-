
# Importa la clase Curso desde la carpeta clases
from clases.curso import Curso

# Función principal: muestra ejemplos de inscripción, eliminación y estado del curso
def main():
    # Crear una instancia del curso
    curso = Curso("Informática")

    # Inscribir alumnos en el curso
    print(curso.inscribir("Miguel"))
    print(curso.inscribir("Antonio"))
    print(curso.inscribir("Miguel"))   # ya inscrito

    # Mostrar la lista actual de alumnos ordenada alfabéticamente
    print("\nLISTA DE ALUMNOS:")
    for alumno in curso.listar():
        print(f"- {alumno}")

    # Remover alumnos del curso
    print("\nREMOVER:")
    print(curso.remover("Pedro"))   # no inscrito
    print(curso.remover("Antonio"))

    # Mostrar el estado final del curso con los alumnos restantes
    print("\nESTADO:")
    print(curso.estado())

if __name__ == "__main__":
    main()