def czy_pierwsza(l):
    if l < 2:
        return False
    i = 2
    while i**2 < l/2:
        if l % i == 0:
            return False
        i += 1
    return True

print(czy_pierwsza(16))