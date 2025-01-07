def last_digit_of_quotient(a, b):
    if b - a >= 5:
        return 0
    else:
        result = 1
        for i in range(a + 1, b + 1):
            result *= i
            result %= 10  # We only care about the last digit
        return result

# Reading input in the standard input format
a, b = map(int, input().split())
print(last_digit_of_quotient(a, b))
