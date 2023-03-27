"""
Wyszukiwanie binarne - szybsze niż liniowe

Złożoność obliczeniowa: O(log)
"""
import math


def wyszukaj_binarnie_reku(t: list, l, p, sz):
    if p>=l:
        sr = (l+p)//2
        if t[sr] == sz:
            return sr
        if t[sr] > sz:
            return wyszukaj_binarnie_reku(t, l, sr - 1, sz)
        else:
            return wyszukaj_binarnie_reku(t, sr + 1, p, sz)
    else:
        return -1

def wyszukaj_binarnie_iter(t, sz):
    l, p = 0, len(t) - 1
    while l<=p:
        sr = l+p//2
        if t[sr] == sz:
            return sr
        if t[sr] > sz:
            p = sr - 1
        else:
            l = sr + 1

    return -1

tablica = [
    0, 10, 30, 50, 70
]
print(wyszukaj_binarnie_reku(tablica, 0, 4, 0))
print(wyszukaj_binarnie_iter(tablica, 0))

