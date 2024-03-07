def es_numero_entero(cadena):
    return cadena.isdigit() #función que permite leer si es dígito o no

texto = input("Ingrese un texto o un número: ")

if es_numero_entero(texto):
    print("Es un número entero")

else:
    print("No es un número entero")


  
