mi_dict = {
    "Colombia": "Bogotá",
    "Alemania": "Berlin",
    "España": "Madrid",
    23: "Jordan",
    "maravillas": 7
}

print(mi_dict)
print(mi_dict["Colombia"])

mi_dict["Italia"] = "Lisboa"
print(mi_dict)

mi_dict["Italia"] = "Roma"
print(mi_dict)

del mi_dict["Alemania"]
print(mi_dict)

mi_tupla = ("Colombia", "Peru", "Argentina")
mi_otro_dict = {
    mi_tupla[0] : "Bogota",
    mi_tupla[1] : "Lima",
    mi_tupla[2] : "Buenos Aires"
}
print(mi_otro_dict)