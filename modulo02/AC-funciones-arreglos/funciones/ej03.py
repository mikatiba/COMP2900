def fahrenheit_a_celsius(fahrenheit):
    temperatura = (fahrenheit - 32) * 0.5556 #operación matemática para determinar la temperatura

    return round(temperatura,1)#función round permite redondear el resultado

temperatura = float(input("Ingrese la temperatura en grados Fahrenheit: "))

resultado = fahrenheit_a_celsius(temperatura)

print(f'La conversión de grados Fahrenheit a Celsius es: {resultado} grados.')


