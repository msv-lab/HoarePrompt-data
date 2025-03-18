def func_1(n: int) -> int:
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total
assert func_1(345) == 12
assert func_1(12) == 3
assert func_1(97) == 16