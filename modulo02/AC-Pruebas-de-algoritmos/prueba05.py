def buscar_elemento(arreglo, elemento):
    return elemento in arreglo
# Prueba
arreglo = [1, 2, 3, 4, 5]
assert buscar_elemento(arreglo, 3), "El elemento no fue encontrado cuando debería."
assert not buscar_elemento(arreglo, 2), "El elemento fue encontrado cuando no debería."