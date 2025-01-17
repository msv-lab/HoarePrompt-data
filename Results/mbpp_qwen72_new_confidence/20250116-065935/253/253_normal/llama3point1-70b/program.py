import math

def sum_Of_product(n):
    """
    Calculate the sum of the product of consecutive binomial co-efficients.

    Args:
        n (int): The number of terms to consider.

    Returns:
        int: The sum of the product of consecutive binomial co-efficients.
    """
    total = 0
    for i in range(1, n + 1):
        total += math.comb(n, i) * math.comb(n, i - 1)
    return total
