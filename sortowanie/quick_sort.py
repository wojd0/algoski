from random_tab import random_tab


def quick_sort(arr):
    smaller = []
    bigger = []
    equal = []
    if len(arr) <= 1:
        return arr

    piwo = arr[0]

    for x in arr:
        if x > piwo:
            bigger += [x]
        elif x == piwo:
            equal += [x]
        else:
            smaller += [x]
    return quick_sort(smaller) + equal + quick_sort(bigger)

tablica = random_tab()
print(quick_sort(tablica))
