def large_product(list1, list2, n):
    products = [a * b for a in list1 for b in list2]
    products.sort(reverse=True)
    return products[:n]

# Test cases to validate the solution
assert large_product([1, 2, 3, 4, 5, 6], [3, 6, 8, 9, 10, 6], 3) == [60, 54, 50]
assert large_product([1, 2, 3, 4, 5, 6], [3, 6, 8, 9, 10, 6], 4) == [60, 54, 50, 48]
assert large_product([1, 2, 3, 4, 5, 6], [3, 6, 8, 9, 10, 6], 5) == [60, 54, 50, 48, 45]
