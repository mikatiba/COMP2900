array = [1, 2, 3, 4, 5, 6, 7]

elementoIngresar = int(input("Ingrese el índice: "))#captura el índice

if(elementoIngresar < 0 or elementoIngresar > (len(array))): #elemento mayor que 0 o elemento mayor que el tamaño del array
    print("El índice no ha sido encontrado.")

else:
    indice = array.index(elementoIngresar) #saca el indice el elemento
    print(f'El indice que ha sido encontrado es: {indice}')



