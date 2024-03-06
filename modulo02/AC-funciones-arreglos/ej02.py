def area_triangulo(base, altura):
    return(base * altura /2) #fórmula matemática para determinar el área del triángulo

#ingresar valores
base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))

resultado = area_triangulo(base, altura)

print(f'El resultado del area del triángulo es: {resultado}') #imprime el resultado


