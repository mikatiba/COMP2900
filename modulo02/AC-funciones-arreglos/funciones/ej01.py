def maximo(val1, val2):
    if(val1 > val2): #si val1 es mayor que val2 imprime val1
        return(val1)

    else:
        return(val2) #si no imprime val2

val1 = input("Ingrese el primer valor: ")
val2 = input("Ingrese el segundo valor: ")

resultado = maximo (val1,val2)

print(f"El máximo entre los dos valores es: {resultado}")

