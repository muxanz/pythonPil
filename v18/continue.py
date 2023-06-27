cadena = "Alfa Romeo"
#print(len(cadena))

contador = 0

for i in cadena:
    if i == " ":
        continue
    contador += 1

print(contador)