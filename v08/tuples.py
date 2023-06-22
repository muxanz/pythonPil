mi_tupla = ("World", 13.3, 2023, 13.3)
print(mi_tupla)

mi_lista = list(mi_tupla)
print(mi_lista)

print(2023 in mi_tupla)
print(mi_tupla.count(13.3))
print(len(mi_tupla))
print(mi_tupla.index(2023))

otra_tupla = (22,)
print(type(otra_tupla))

# desempaquetado de tupla
persona = ("Lorena", 22, "Barcelona", 58.8)

nombre, edad, ciudad, peso = persona
print("nombre: ", nombre, "\nEdad: ", edad, "\nCiudad: ", ciudad, "\nPeso: ", peso)