# Count array elements in recursive
# Asymptotic complexity (O) = n


def count_recursive(arr):
    """
    :type arr: list
    :rtype: int
    """
    if not arr:
        return 0

    return 1 + count_recursive(arr[1:])


print(count_recursive([2, 4, 5, 7, 1, 6]))  # 6
