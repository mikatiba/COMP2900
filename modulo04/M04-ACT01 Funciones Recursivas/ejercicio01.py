def suma_naturales(n):
    if n == 1:
        return 1 

    else:
        return n + suma_naturales(n-1)

print(suma_naturales(2))

