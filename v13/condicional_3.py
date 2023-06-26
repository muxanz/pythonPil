print("-----Electivas 2023-----")
print("""
Seleccione una:
  - Pruebas de Software
  - Informatica grafica
  - Arquitectura de Hardware
""")

opcion = input("Digita la electiva seleccionada: ")

electiva = opcion.lower()

if electiva in ("pruebas de software", "informatica grafica", "arquitectura de hardware"):
    print("Electiva seleccionada: " + electiva)
else:
    print("Electiva no encontrada !!")