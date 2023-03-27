"""
Wyszukiwanie wzorca - wyszukiwanie wyrazu w wyrazie, np. motyw występuje w lokomotywie
"""

def wyszukaj_wzorzec(wz, tek):
    # Tyle pierwszych liter w tekście trzeba sprawdzić, bo gdyby wzorzec
    # miał się zacząć na następnych, to by się nie zmieścił. Ot skip
    max = len(tek) - len(wz) + 1
    i=0
    for i in range(0, max):
        k = 0
        for j in range(i, len(wz) - 1 + i):
            if(tek[j] != wz[k]):
                break
            k += 1
        else:
            return f'Wzór znaleziony od miejsca {i}'

    return 'Brak wzorca w tekscie'

print(wyszukaj_wzorzec('algorytm', 'wyalgorytmika'))
