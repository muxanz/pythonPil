import math

print("****RAIZ CUADRADA****")

num = int(input("Ingrese un número: "))

intentos = 0

while num < 0:
    print("No es posbile hallar raiz cuadrada a números negativos!!")

    if intentos == 2:
        print("Se han alcanzado el maximo de intentos")
        break
    
    intentos += 1

    num = int(input("Ingrese un número: "))

if num > 0:
    resultado = math.sqrt(num)
    print(f"La raiz cuadrada de {num} es {resultado}")

print("Fin de la ejecución...")