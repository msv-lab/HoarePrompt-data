import math

def is_perfect_square(n: int) -> bool:
    if n < 0:
        return False
    sqrt_n = int(math.isqrt(n))
    return sqrt_n * sqrt_n == n

# Testing the function with the provided assertions
assert not is_perfect_square(10)
assert is_perfect_square(36)
assert not is_perfect_square(14)
assert is_perfect_square(14*14)
assert not is_perfect_square(125)
assert is_perfect_square(125*125)
