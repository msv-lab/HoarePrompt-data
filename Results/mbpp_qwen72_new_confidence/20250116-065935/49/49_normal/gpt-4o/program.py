def divisor(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

# Test cases
assert divisor(15) == 4  # Divisors: 1, 3, 5, 15
assert divisor(12) == 6  # Divisors: 1, 2, 3, 4, 6, 12
assert divisor(9) == 3   # Divisors: 1, 3, 9
