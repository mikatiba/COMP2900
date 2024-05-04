def busqueda_secuencial(lista, elemento_a_buscar):
    index = 0 #se inicializa en 0
    for elemento in lista:
        if elemento == elemento_a_buscar: #si el elemento es igual a elemento a buscar devuelve el índice
            return index 
        index += 1 #lo mismo que index = index +1
    return -1

