# Find max element in array with recursive
# Asymptotic complexity (O) = n


def max_recursive(arr):
    """
    :type arr: list
    :rtype: int
    """
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]

    max = max_recursive(arr[1:])
    return arr[0] if arr[0] > max else max


print(max_recursive([2, 4, 5, 7, 1, 6]))  # 7
