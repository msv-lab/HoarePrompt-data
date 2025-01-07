def func_1(s):
    q = (math.sqrt(5) + 1) / 2
    decimal = 0
    for (i, c) in enumerate(reversed(s)):
        decimal += int(c) * q ** i
    return decimal
a = input()
b = input()
decimal_a = func_1(a)
decimal_b = func_1(b)
if decimal_a > decimal_b:
    print('>')
elif decimal_a < decimal_b:
    print('<')
else:
    print('=')