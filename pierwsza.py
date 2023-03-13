def czy_pierwsza(n: int):
    if n < 2:
        return False

    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            return False
        i+=1

    return True

print(czy_pierwsza(4))
