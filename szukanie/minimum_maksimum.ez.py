def wyszukaj_min(tab):
    min = tab[0]
    for n in tab[1:]:
        if n < min:
            min = n
    return min

def wyszukaj_max(tab):
    max = tab[0]
    for n in tab[1:]:
        if n > max:
            max = n
    return max

def min_max(tab):
    min, max = tab[0], tab[0]
    for n in tab[1:]:
        if n > max:
            max = n
        if n < min:
            min = n
    return min, max

tablica = [2, 25, 3, 20, 10, 3, 46, 40, 36, 43]

print(wyszukaj_min(tablica))
print(wyszukaj_max(tablica))
print(min_max(tablica))