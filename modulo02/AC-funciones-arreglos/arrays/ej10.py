array = [2, 4, 6, 8, 10, 12]
print(f'Arreglo original: {array}')

ultimoElemento = array[-1] #obtiene el último elemento del arreglo
for elemento in range(len(array) -1, 0, -1):
    array[elemento] = array[elemento - 1] #permite mover cada elemento a la derecha

array[0] = ultimoElemento #permite ubicar el último elemento en la primera posición

print(f'Arreglo con una rotación a la derecha {array}')