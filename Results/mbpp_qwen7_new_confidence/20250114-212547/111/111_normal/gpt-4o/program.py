import math

def next_Perfect_Square(n):
    next_root = math.ceil(math.sqrt(n))
    return next_root ** 2

# Testing the function with the provided test cases
assert next_Perfect_Square(35) == 36
assert next_Perfect_Square(6) == 9
assert next_Perfect_Square(9) == 16
