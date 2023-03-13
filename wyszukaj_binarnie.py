"""
Wyszukiwanie binarne - szybsze niż liniowe

Złożoność obliczeniowa: O(log)
"""

def wyszukaj_binarnie(t: list, l, p, sz):
    if p>=l:
        sr = (l+p)//2

        if t[sr] == sz:
            return sr
        if t[sr] > sz:
            return wyszukaj_binarnie(t, l, sr-1, sz)
        else:
            return wyszukaj_binarnie(t, sr + 1, p, sz)
    else:
        return -1

print(wyszukaj_binarnie([
    0, 10, 30, 50, 70
], 0, 4, 30))