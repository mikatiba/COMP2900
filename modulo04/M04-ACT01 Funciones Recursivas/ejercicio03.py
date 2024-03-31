def MCD(val1,val2):
    if val2 == 0: #si el valor 2 es igual a 0 retorna el valor 1
        return val1

    else:
        resultado = MCD(val2, val1 % val2) #si no devuelve esta operación 
        return resultado

print(MCD(18,6))
print(MCD(5, 125))
print(MCD(20, 24))
print(MCD(300, 0))