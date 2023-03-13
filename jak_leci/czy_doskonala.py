def czy_doskonala(l):
    s, sqrt = 1, l ** 0.5
    i = 2
    while i <= sqrt:
        if l % i == 0:
            s += i + l / i
        i += 1

    if l == sqrt*sqrt:
        s -= sqrt

    if s == l:
        return True
    return False

print(czy_doskonala(6))