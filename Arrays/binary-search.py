def binary_search(arr, find):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = int((low + high) / 2)
        check = arr[mid]
        if check == find:
            return mid
        elif check > find:
            high = mid - 1
        else:
            low = mid + 1
    return None


arr = [1, 3, 6, 8, 9, 11, 15]
print(binary_search(arr, 6))
print(binary_search(arr, -5))
