import timeit
# Encontrar el número más grande en una lista de números. 
# Enfoque 1: Utilizando la función max() de Python para encontrar el # número más grande en una lista.
def max_lista(lista): 
    return max(lista)


numbers = list(range(1,1001))
time_for = timeit.timeit(lambda: max_lista(numbers), number=10000)
print("Enfoque 1: ", time_for)

# Enfoque 2: Recorriendo la lista y comparando cada número con un valor # de referencia para encontrar el número más grande 
def max_iterativo(lista):
    maximo = lista[0]
    for numero in lista:
        if numero > maximo:
            maximo = numero
    return maximo

time_genexp = timeit.timeit(lambda: max_iterativo(numbers), number=10000)
print("Enfoque 2: ", time_genexp)

