def invertir_cadena(cadena):
    array_length = len(cadena)#el tamaño de la cadena
    nueva_cadena = ''
    for i in range(array_length):#determina los índices del rango
        nueva_cadena += (cadena[array_length-1-i])
    return nueva_cadena

mensaje = 'Hola mi nombre es Mikael'
print(mensaje)
print(invertir_cadena(mensaje))





