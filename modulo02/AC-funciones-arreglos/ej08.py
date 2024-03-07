def contar_vocales(cadena):
    contador_vocales = 0

    for letra in cadena:
        if letra.lower() in "aeiou":

            contador_vocales +=1

    return contador_vocales


print(contar_vocales("HOLA mi nombre es Mikael!"))

    