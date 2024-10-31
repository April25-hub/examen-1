print("Arzaba Diaz April")
print("1173")
print("3W")
#esta linea me dara un diccionario con los creditos de las asignaturas
asignaturas = {'Matematicas': 6, 'Fisica': 4, 'Quimica': 5}

#esta linea iniciara un contador para los creditos totales
total_creditos = 0

#esta linea mostrara los creditos de cada asignatura
for asignatura, creditos in asignaturas.items():
    print(f"{asignatura} tiene {creditos} creditos")
    total_creditos += creditos

#esta linea mostrara el total de creditos del curso
print(f"Total de creditos del curso: {total_creditos}")
