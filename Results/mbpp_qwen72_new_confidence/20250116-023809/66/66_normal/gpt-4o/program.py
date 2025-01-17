def max_product_tuple(lst):
    max_product = 0
    for a, b in lst:
        product = abs(a * b)
        if product > max_product:
            max_product = product
    return max_product

# Test cases
import math
assert math.isclose(max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]), 36, rel_tol=0.001)
assert math.isclose(max_product_tuple([(10,20), (15,2), (5,10)] ), 200, rel_tol=0.001)
assert math.isclose(max_product_tuple([(11,44), (10,15), (20,5), (12, 9)] ), 484, rel_tol=0.001)
