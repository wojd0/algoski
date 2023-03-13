wynik = ''
def zamiana (l, p):
    global wynik
    if l != 0:
        zamiana(l//p, p)
        wynik += str(l % p)

zamiana(12, 4)
print(wynik)