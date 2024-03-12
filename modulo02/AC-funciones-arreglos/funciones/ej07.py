def es_numero_entero(cadena):
    for char in cadena:
        if char < '0' or char > '9': #si char es menor que 0 o char es mayor que 9 se ejectua la lína debajo
            return print('El valor ingresado es de tipo carácter')
        
        return print('El valor ingresado es de tipo entero')

texto = input("Ingrese un texto o un número: ")
es_numero_entero(texto)#se llama la función y se le devuelve parámetro

        

 





  
