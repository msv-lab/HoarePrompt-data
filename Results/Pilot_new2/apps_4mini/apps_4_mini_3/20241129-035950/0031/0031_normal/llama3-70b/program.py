def calculate_probability(n, k):
    total_days = 2 ** n
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator *= (total_days - i)
        denominator *= (total_days)
    gcd = math.gcd(numerator, denominator)
    numerator //= gcd
    denominator //= gcd
    return numerator % (10**6 + 3), denominator % (10**6 + 3)

n, k = map(int, input().split())
A, B = calculate_probability(n, k)
print(A, B)
