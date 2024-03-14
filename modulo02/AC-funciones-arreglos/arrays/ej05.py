array = [2, 4, 6, 8, 10, 12, 14, 16]

print(array)
elementoEliminar = int(input("Ingrese el elemento que desea eliminar: ")) #captura el elemento

newArray = [] #array vacío

for elemento in array:
    if elemento !=elementoEliminar: #si el elemento no es ElementoEliminar
        newArray.append(elemento)

print(f'El elemento a eliminar es {elementoEliminar}, lista actualizada: {newArray}')


        

