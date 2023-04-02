from random_tab import random_tab


def merge_sort(array):
    if len(array) <= 1:
        return array

    midpoint = len(array) // 2

    left, right = merge_sort(array[:midpoint]), merge_sort(array[midpoint:])

    return merge(left, right)

def merge(left, right):
    result = []

    left_p = right_p = 0

    while left_p < len(left) and right_p < len(right):
        if left[left_p] < right[right_p]:
            result.append(left[left_p])
            left_p += 1
        else:
            result.append(right[right_p])
            right_p += 1

    result += left[left_p:]
    result += right[right_p:]

    return result

tablica = random_tab()

print(merge_sort(tablica))