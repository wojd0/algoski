def dopelnij_cyfrowo(n):
    suma = 0
    kopia = n
    while kopia > 0:
        kopia = kopia // 10
        suma = suma * 10 + 9

    return suma - n

print(dopelnij_cyfrowo(333))