array = [1,2 ,3, 4, 5, 3, 3, 4, 5, 6, 3, 3]

contadorNum = 0

for num in array:
    if(num == 3): #si el número es igual a 3 se incrementa
        contadorNum += 1

print(f"El número 3 aparece {contadorNum} veces en la lista.")