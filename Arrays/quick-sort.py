# Quick sort array
# Asymptotic complexity (O) = n * n


def quick_sort(arr):
    """
    :type arr: list
    :rtype: list
    """
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([5, 1, 7, 2, 9, 3]))  # [1, 2, 3, 5, 7, 9]
