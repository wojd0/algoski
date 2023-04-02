from random_tab import random_tab


def selection_sort(tab):
    size = len(tab)

    for i in range(0, size):
        min_index = i
        for j in range(i, size):
            if tab[min_index] > tab[j]:
                min_index = j
        tab[i], tab[min_index] = tab[min_index], tab[i]

    return tab


tab = random_tab()
print(selection_sort(tab))