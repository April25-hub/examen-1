print("Arzabza Diaz April")
print("1173")
print("3W")
#esta linea me dara la ista de asignaturas
asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]

#esta linea me dara un diccionario para guardar las notas
notas = {}

#esta linea preguntara al usuario por la nota en cada asignatura
for asignatura in asignaturas:
    nota = float(input(f"ingrese la nota en {asignatura}: "))
    notas[asignatura] = nota

#esta linea eliminara las asignaturas aprobadas (considerando aprobado >= 6)
asignaturas_repetir = [asignatura for asignatura, nota in notas.items() if nota < 6]

#esta linea mostrara las asignaturas que hay que repetir
print("asignaturas que hay que repetir:")
for asignatura in asignaturas_repetir:
    print(asignatura)



