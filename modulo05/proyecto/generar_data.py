# Generar Datos
import random

#permite generar lista de datos de manera ordenada
def mejor_caso():
    f = open("mejor_caso.dat", "a")
    for n in range(1, 100001):
        f.write(f"{n}\n")
    f.close()

#permite generar datos de manera inversa
def peor_caso():
    f = open("peor_caso.dat", "a")
    for n in range(100000,0, -1):
        f.write(f"{n}\n")
    f.close()

#permite generar datos aleatoriamente utilizando random.randit
def caso_promedio():
    f = open("promedio_caso.dat", "a")
    for n in range(1, 100001):
        numero = random.randint(1, 100001)
        f.write(f"{numero}\n")
    f.close()

#llamada a las funciones
mejor_caso()
peor_caso()
caso_promedio()