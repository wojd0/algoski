import random

from random_tab import random_tab


def bogo_sort(arr):
    n, i = len(arr), 0
    while jest_posortowane(arr) == False:
        mix(arr)
        i += 1

    return arr, i

def jest_posortowane(arr):
    n = len(arr)
    for i in range(0, n-1):
        if arr[i] > arr[i+1]:
            return False
    return True

def mix(arr):
    n = len(arr)
    for i in range(n):
        r = random.randint(0, n-1)
        arr[i], arr[r] = arr[r], arr[i]

tablica = random_tab()
print(bogo_sort(tablica[:10]))