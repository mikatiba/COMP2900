def contar_apariciones_letra(cadena, letra):
    contador_letra = 0 #almacena la aparición de la letra escogida

    for cadena in cadena:
        if cadena.lower() == letra.lower(): 

            contador_letra +=1 #se incrementa
    return contador_letra


print(contar_apariciones_letra("Este año sacaré A en todas las clases!", "a"))