#con funcion
def genera_pares(limite):
    i = 1
    pares = []

    while i < limite:
        pares.append(i  * 2)
        i += 1
    
    return pares

print(genera_pares(10))

#con generaodor
def genera_pares_g(limit):
    j = 1

    while j < limit:
        yield j * 2
        j += 1

mis_pares = genera_pares_g(10)

#print(type(mis_pares)) <class 'generator'>

# for i in mis_pares:
#     print(i, end=" ")

print(next(mis_pares))
print("mas codigo")
print(next(mis_pares))
print("mas codigo")
