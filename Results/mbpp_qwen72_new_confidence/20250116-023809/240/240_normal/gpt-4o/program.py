from functools import reduce
from operator import mul

def unique_product(numbers):
    # Convert the list to a set to obtain unique elements
    unique_numbers = set(numbers)
    
    # Calculate the product of the unique elements
    product = reduce(mul, unique_numbers, 1)
    
    return product

# Test cases
assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) == 720000000
assert unique_product([1, 2, 3, 1]) == 6
assert unique_product([7, 8, 9, 0, 1, 1]) == 0
