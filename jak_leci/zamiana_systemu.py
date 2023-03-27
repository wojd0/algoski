wynik = ''
def zamiana (n, p):
    if n != 0:

        return str(n % p) + (zamiana(n // p, p) or '')

print(zamiana(20, 6))
