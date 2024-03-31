def coeficienteBinomial(n, k):
    if k == 0 or k == n:
        return 1

    else:
        resultado = coeficienteBinomial(n -1, k-1) + coeficienteBinomial(n-1, k)
        return resultado

print(coeficienteBinomial(5,2))
print(coeficienteBinomial(5,4))
print(coeficienteBinomial(3,3))
