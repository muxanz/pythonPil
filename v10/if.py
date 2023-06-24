print("ingrese nota del alumno: ")
nota = int(input())

def eval(nota):
    valoracion = "aprobado"
    if nota < 5:
        valoracion = "pendiente"
    return valoracion

print(eval(nota))