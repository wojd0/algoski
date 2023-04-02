def czy_doskonala(n):
    s, sqrt = 1, n ** 0.5
    i = 2
    while i <= sqrt:
        if n % i == 0:
            s += i + n / i
        i += 1

    if n == sqrt*sqrt:
        s -= sqrt

    if s == n:
        return True
    return False

print(czy_doskonala(6))