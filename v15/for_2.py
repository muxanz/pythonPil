mi_email = input("Ingrese email: ")

contador = 0

for i in mi_email:
    if i == "@" or i == ".":
        contador += 1

if contador >= 2:
    print("Email correcto")
else:
    print("Email no es correcto")