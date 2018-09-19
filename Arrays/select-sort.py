# Selection sort of array
# Asymptotic complexity (O) = n * n


def find_smallest_index(arr):
    smallest, smallest_index = arr[0], 0
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest, smallest_index = arr[i], i
    return smallest_index


def select_sort(arr):
    sort_arr = []
    for i in range(len(arr)):
        sort_arr.append(arr.pop(find_smallest_index(arr)))
    return sort_arr


print(select_sort([2, 4, 5, 7, 1, 6]))  # [1, 2, 4, 5, 6, 7]
