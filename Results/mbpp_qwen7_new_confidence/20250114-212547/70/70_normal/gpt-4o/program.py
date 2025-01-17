def sum_common_divisors(a, b):
    def divisors(n):
        divs = set()
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divs.add(i)
                divs.add(n // i)
        return divs
    
    divisors_a = divisors(a)
    divisors_b = divisors(b)
    common_divisors = divisors_a & divisors_b
    
    return sum(common_divisors)

# Test cases
assert sum_common_divisors(10, 15) == 6
assert sum_common_divisors(100, 150) == 93
assert sum_common_divisors(4, 6) == 3
