array = [2, 4, 6, 8, 10, 12]

suma = 0 # se inicializa en 0
arrayLength = len(array) #tamaño de la lista
for num in array: #permite que la variable itere sobre la lista sumando los valores
    suma += num

promedio = (suma / arrayLength) #se divide la suma del array entre el tamaño del array

print(f'El promedio de los elementos del arreglo {array} es {promedio}.')
