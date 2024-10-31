print("Arzaba Diaz April")
print("1173")
print("3W")
#esta linea ara una lista de asignaturas
asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]

#esta linea ara un diccionario para almacenar las notas
notas = {}

#esta linea areguntara al usuario la nota de cada asignatura
for asignatura in asignaturas:
    nota = input(f"introduce la nota que has sacado en {asignatura}: ")
    notas[asignatura] = nota

#esta linea mostrara los resultados
for asignatura, nota in notas.items():
    print(f"en {asignatura} has sacado {nota}")
