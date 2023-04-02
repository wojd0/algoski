def horner(wsp, st, x):
    wynik = wsp[0]

    for i in range(1, st+1):
        wynik = wynik*x + wsp[i]

    return wynik

print(horner([3, 3, -2, 11], 3, 2))