import math

def golden_to_decimal(s):
    q = (math.sqrt(5) + 1) / 2
    decimal = 0
    for i, c in enumerate(reversed(s)):
        decimal += int(c) * (q ** i)
    return decimal

a = input()
b = input()

decimal_a = golden_to_decimal(a)
decimal_b = golden_to_decimal(b)

if decimal_a > decimal_b:
    print('>')
elif decimal_a < decimal_b:
    print('<')
else:
    print('=')
