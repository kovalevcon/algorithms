# Factorial
# Asymptotic complexity (O) = n


def fact(x):
    """
    :type x: int
    :rtype: int
    """
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


print(fact(3))  # 6
