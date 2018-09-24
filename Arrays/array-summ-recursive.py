# Summary array elements in recursive
# Asymptotic complexity (O) = n * n


def array_sum_recursive(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]

    return arr.pop(0) + array_sum_recursive(arr)


print(array_sum_recursive([2, 4, 5, 7, 1, 6]))  # 25
