def promedio(lista_numeros):
    suma = 0
    array_length = 0
    for valor in lista_numeros:
        suma += valor
        array_length += 1

    return(suma / array_length)

lista = []
for i in range(6):
    valores = float(input("Ingrese un valor: "))
    lista.append(valores)

resultado = promedio(lista)
print(f'El promedio de la lista: {resultado}')












