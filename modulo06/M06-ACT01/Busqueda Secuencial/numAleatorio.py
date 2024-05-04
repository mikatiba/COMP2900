import random 
from busqueda_secuencial import busqueda_secuencial #se importó la función de búsqueda
#función para generar números aleatorios
def numeros_aleatorios(numeros):
    lista_numeros = [] #lista vacía
    for i in range(numeros):
        numero = random.randint(1,100) #permite generar números 
        lista_numeros.append(numero) #añade numeros a la lista vacía
    return lista_numeros #devuelve la lista

#se hace llamada a la función cuyo rango es de 10 elementos
numeros_generados = numeros_aleatorios(10)
print(numeros_generados)

#usuario ingresa el elemento a buscar
numUsuario = int(input("Ingrese el número deseado: "))

indice = busqueda_secuencial(numeros_generados, numUsuario)

#si el índice es negación de -1
if indice != -1:
    print(f"El número {numUsuario} se encuentra en la posición {indice} de la lista generada.")

else:
    print(f"El número {numUsuario} no se encuentra en la lista generada. ")


