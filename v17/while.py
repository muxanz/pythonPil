edad = int(input("Ingrese la edad: "))

while edad < 5 or edad > 100:
    print("Edad incorrecta!!, vuelva a intentarlo.")
    edad = int(input("Ingrese la edad: "))

print("Edad validada, puede continuar...")
print(f"Edad aspirante {edad}")