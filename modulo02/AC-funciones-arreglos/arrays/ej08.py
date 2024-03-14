array = [18, 30, 22, 32, 40, 12, 6, 8]

tamañoLista = len(array) #determina el tamaño del array

for elemento in range(tamañoLista): #recorre desde 0 hasta el tamañoLista - 1
    for no_elemento in range(0, tamañoLista-elemento-1): #La cantidad de iteraciones se reduce en cada paso para evitar que se vuelvan a comprarar
        if array[no_elemento] > array[no_elemento+1]:
            array[no_elemento], array[no_elemento+1] = array[no_elemento+1], array[no_elemento] #si el elemento actual es mayor que el siguiente, se cambian

#imprime la lista de manera ordenada
print('Lista ordenada: ')
for elemento in array:
    print(elemento, end=' ')
