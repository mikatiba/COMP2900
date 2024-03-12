def contar_apariciones_letra(cadena, letra):
    contador_letra = 0 #almacena la aparición de la letra escogida

    for char in cadena:
        if char.lower() in letra.lower(): #convierte la cadena en minúscula y letra.lower() busca la a
            contador_letra +=1 #se incrementa
            
    return contador_letra


print(contar_apariciones_letra("Este año sacaré A en todas las clases!", "a"))