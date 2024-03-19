def encontrar_indice(lista, elemento):
    if (elemento in lista): #si el elemento esta en lista devuelve el indice
        return lista.index(elemento)

    else: 
        return -1 #si no devuelve -1

miLista = [2, 4, 6, 8, 10, 12]
print(miLista)
numeroIngresar = int(input("Ingrese un número: ")) #captura valor de tipo entero

valorEncontrado = encontrar_indice(miLista, numeroIngresar)

if(valorEncontrado > -1): #si el valor es mayor que -1 ejecuta la línea de comando
    print(f'El índice de la lista es: {valorEncontrado}')

else:
    print("El índice no está en la lista.")


    
       


   







    

    
