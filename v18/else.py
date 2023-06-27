email = input("ingresa email: ")

for i in email:
    if i == "@":
        arroba = True
        break
else:
    arroba = False

print(f"Tiene arrob@ ? {arroba}")