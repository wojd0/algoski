from random_tab import random_tab


def insertion_sort(tab):
    size = len(tab) - 1
    for i in range(1, size):
        x = tab[i]
        j = i - 1
        while j >= 0 and x < tab[j]:
            tab[j+1] = tab[j]
            j -= 1
        tab[j+1] = x
    return tab


tab = random_tab()
insertion_sort(tab)
print(tab)
