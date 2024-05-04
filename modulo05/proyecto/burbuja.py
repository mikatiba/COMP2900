import timeit
#estructura Bubble Sort
def bubble_sort(arr):
    n = len(arr) #tamaño del arreglo
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
#comienza en 10,000 para en 110000 e incrementa en 10000
for corridas in range(10000, 110000, 10000):
    print(f'Organizando {corridas} datos ... Favor esperar')
    lista = []
    f = open("promedio_caso.dat", "r")
    for n in f:
        lista.append(n)
    f.close()

    del lista[corridas:] # 10000 elementos (debe borrar 90000 elementos)

    tiempo = timeit.timeit(lambda:bubble_sort(lista),number=1)#permite medir el tiempo
    print(f'Tiempo: {tiempo} segs')