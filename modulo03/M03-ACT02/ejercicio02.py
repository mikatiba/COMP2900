import timeit
# Suma de todos los números enteros de 1 a un número determinado n.
# Enfoque 1: usando un ciclo for para recorrer todos los números # de 1 a n y sumarlos
def suma_for(n):
    suma = 0
    for i in range(1, n+1):
        suma += i
    return suma

numbers = list(range(1,1001))
time_for = timeit.timeit(lambda: suma_for(1000), number=10000)
print("Enfoque 1: ", time_for)

# Enfoque 2: fórmula matemática para calcular la suma de # una serie aritmética
def suma_formula(n):
    return (n * (n+1)) // 2

time_genexp = timeit.timeit(lambda: suma_for(1000), number=10000)
print("Enfoque 2: ", time_genexp)