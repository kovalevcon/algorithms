# Quick sort array with random pivot item
# Asymptotic complexity (O) = n log n
import random


def quick_sort_random(arr):
    """
    :type arr: list
    :rtype: list
    """
    if len(arr) < 2:
        return arr
    else:
        item = random.randrange(0, len(arr))
        pivot = arr[item]
        arr = arr[:item] + arr[item + 1:]
        less = [i for i in arr if i <= pivot]
        greater = [i for i in arr if i > pivot]

        return quick_sort_random(less) + [pivot] + quick_sort_random(greater)


print(quick_sort_random([5, 1, 7, 2, 9, 3]))  # [1, 2, 3, 5, 7, 9]
