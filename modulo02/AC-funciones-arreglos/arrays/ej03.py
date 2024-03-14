array = [1, 2, 3, 4, 5, 6, 7]
array_length = len(array)
new_array = []

for num in range(array_length):
    new_array.append(array[array_length -1 -num]) #se utiliza para acceder al último elemento de la lista 
print(f'El orden de los elementos: {array}')
print(f'El orden invertido de los elementos del arreglo es: {new_array}')