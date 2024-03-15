import math
def calcular_area_circulo(radio):
    return math.pi * radio ** 2
    # Prueba
    
assert calcular_area_circulo(2) == math.pi, "El área calculada no es correcta."