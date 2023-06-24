print("***Verificación de Acceso***")

edad_usuario = int(input("ingrese edad: "))

if edad_usuario < 18:
    print("No puede ingresar")
elif edad_usuario > 100:
    print("Edad incorrecta")
else:
    print("Puede ingresar")

print("**Fin verificación**")