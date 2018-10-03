# Summary array elements in recursive
# Asymptotic complexity (O) = n


def sum_recursive(arr):
    """
    :type arr: list
    :rtype: int
    """
    if not arr:
        return 0

    return arr[0] + sum_recursive(arr[1:])


print(sum_recursive([2, 4, 5, 7, 1, 6]))  # 25
