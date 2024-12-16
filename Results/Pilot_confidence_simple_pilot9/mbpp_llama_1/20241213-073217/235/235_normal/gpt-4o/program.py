def sum_digits(n: int) -> int:
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

# Testing the function with the provided test cases
assert sum_digits(345) == 12
assert sum_digits(12) == 3
assert sum_digits(97) == 16
