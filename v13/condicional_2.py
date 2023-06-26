print("Becas 2023")

distancia_escuela = int(input("Distancia casa a escuela (KM): "))
cantidad_hermanos = int(input("Cantidad de hermanos: "))
ingresos_familia = int(input("Salario anual bruto: "))

if distancia_escuela > 40 and cantidad_hermanos > 2 or ingresos_familia <= 20000:
    print("Tiene derecho a la beca")
else:
    print("No tiene derecho a la beca")
