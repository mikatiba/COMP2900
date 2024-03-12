def promedio(lista_numeros):
    suma = 0
    array_length = 0
    for valor in lista_numeros: #valor en la lista se incrementa
        suma += valor
        array_length += 1

    return(suma / array_length)

lista = [] #lista vacía
for i in range(6): #permite hasta 6 dígitos
    valores = float(input("Ingrese un valor: "))
    lista.append(valores) #añade valores a la lista vacía

resultado = promedio(lista)
print(f'El promedio de la lista: {resultado}')












