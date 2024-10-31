print("Arzaba Diaz April")
print("1173")
print("3W")
#esta linea solicitara información al usuario
nombre = input("por favor, ingresa tu nombre: ")
edad = input("por favor, ingresa tu edad: ")
direccion = input("por favor, ingresa tu dirección: ")
telefono = input("por favor, ingresa tu número de teléfono: ")

#esta linea guardara la información en un diccionario
informacion_usuario = {
    "nombre": nombre,
    "edad": edad,
    "direccion": direccion,
    "telefono": telefono
}

#esta linea mostrara la información en pantalla
print(f"{informacion_usuario['nombre']} tiene {informacion_usuario['edad']} años, vive en {informacion_usuario['direccion']} y su número de teléfono es {informacion_usuario['telefono']}.")
