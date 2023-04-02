from random_tab import random_tab


def bubble_sort(tab):
    size = len(tab)
    for i in range(size):
        for j in range(1, size - i):
            if tab[j] < tab[j-1]:
                tab[j], tab[j-1] = tab[j-1], tab[j]
    return tab

tab = random_tab()

print(bubble_sort(tab))