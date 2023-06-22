mi_lista = ["Hugo", "Paco", "Luis", "Pedro", "Pepe"]
print(mi_lista)
print(mi_lista[2])
print(mi_lista[-2])
print(mi_lista[3:])
print(mi_lista[2:-1])

mi_lista.append("Sandra")
print(mi_lista)

mi_lista.insert(0, "Clara")
print(mi_lista)

mi_lista.extend(["Thomas", "Kitty", "Moji"])
print(mi_lista)

print(mi_lista.index("Thomas"))

print("Kitty" in mi_lista)
print("Olaf" in mi_lista)


otra_lista = [2, 23.4, True, "Hola", 100, False]
print(otra_lista)

otra_lista.remove("Hola")
print(otra_lista)

otra_lista.pop()
print(otra_lista)


numeros_a = [1, 2, 3, 4, 5]
numeros_b = [6, 7, 8, 9, 10]

numeros_c = numeros_a + numeros_b
print(numeros_c)
