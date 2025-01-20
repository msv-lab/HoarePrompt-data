def max_product(arr):
    n = len(arr)
    if n == 0:
        return 0

    # Initialize a list to store the maximum product up to each element
    max_products = [0] * n
    max_products[0] = arr[0]

    for i in range(1, n):
        max_products[i] = arr[i]
        for j in range(i):
            if arr[j] < arr[i]:
                max_products[i] = max(max_products[i], max_products[j] * arr[i])

    # Return the maximum product found
    return max(max_products)

# Test cases
assert max_product([3, 100, 4, 5, 150, 6]) == 3000
assert max_product([4, 42, 55, 68, 80]) == 50265600
assert max_product([10, 22, 9, 33, 21, 50, 41, 60]) == 2460
