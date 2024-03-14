def clasificar_numero(num):
    if num > 0:
        return "Positivo"
    elif num < 0:
        return "Negativo"
    else:
        return "Cero"

    # Prueba
assert clasificar_numero(5) == "Positivo", "La clasificación no es correcta."
assert clasificar_numero(-1) == "Negativo", "La clasificación no es correcta"
assert clasificar_numero(3) == "Cero", "La clasificación no es correcta"