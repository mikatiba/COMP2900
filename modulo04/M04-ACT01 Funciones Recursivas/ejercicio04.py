def invertirCadena(cadena):
    if len(cadena) <= 1:
        return cadena

    else:
        return invertirCadena(cadena[1:]) + cadena[0]

cad = "Hola soy Mikael"
cadenaInvertida = invertirCadena(cad)

print("Cadena en orden: " + cad)
print("Cadena invetida: " + cadenaInvertida)
