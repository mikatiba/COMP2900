def potenciaNum(base, exponente):
    if exponente == 0: #si el exponente es igual a 0 va a retornar 1
        return 1

    elif exponente == 1: #si el exponente es igual a 1 devuelve la base
        return base

    else:
        return base * potenciaNum(base, exponente -1) #si no retorna esta operación matemática

print(potenciaNum(3,0))
print(potenciaNum(5,3))
print(potenciaNum(10,1))




