import random

def generar_numeros_aleatorios(cantidad, maximo, minimo):
    numeros_aleatorios = [] #se inicializa lista vacía para almacenar números
    for _ in range(cantidad):
        numero_aleatorio = int(random.random() * (maximo - minimo + cantidad + 1)+ minimo)#genera número aleatorio entre 0 y 1
        numeros_aleatorios.append(numero_aleatorio) #agrega valores a la lista

    return numeros_aleatorios

maximo = 10
minimo = 1
cantidad = 10

resultado = generar_numeros_aleatorios(cantidad, maximo, minimo)

print(f"Números aleatorios generados: {resultado}")

