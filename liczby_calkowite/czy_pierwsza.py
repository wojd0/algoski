def czy_pierwsza(n):
    if n < 2:
        return False
    i = 2
    while i**2 < n/2:
        if n % i == 0:
            return False
        i += 1
    return True

print(czy_pierwsza(16))