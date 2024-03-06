def promedio(lista_numeros):

    return (sum(lista_numeros) / len(lista_numeros)) #suma los valores de la lista luego divide por el tamaño de la lista

lista = [] #lista vacía
for i in range(6):
    valores = float(input("Ingrese un valor: "))
    lista.append(valores) #agrega el valor a la lista

resultado = promedio(lista)
print(f"El promedio de la lista: {resultado} ")










