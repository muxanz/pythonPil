email = input("Ingrese email: ")
valido = False

for i in range(len(email)):
    if email[i] == "@":
        valido = True
    
if valido:
    print("Email correcto")
else:
    print("Email no es correcto")