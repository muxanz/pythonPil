def muestra_ciudades(*ciudades):
    for elemento in ciudades:
        #for char in elemento:
        yield from elemento

mis_ciudades = muestra_ciudades("Houston", "Miami", "Vancouver", "Toronto")

print(next(mis_ciudades))
print(next(mis_ciudades))