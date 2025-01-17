def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i * i == n:
                count += 1  # Perfect square case
            else:
                count += 2  # Both i and n // i are divisors
    return count % 2 == 0

# Tests
assert count_divisors(10)
assert not count_divisors(100)
assert count_divisors(125)
