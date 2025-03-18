def func_1(digits, base):
    decimal_value = 0
    for digit in digits:
        decimal_value = decimal_value * base + digit
    return decimal_value
(n, base_x) = map(int, input().split())
digits_x = list(map(int, input().split()))
(m, base_y) = map(int, input().split())
digits_y = list(map(int, input().split()))
decimal_x = func_1(digits_x, base_x)
decimal_y = func_1(digits_y, base_y)
if decimal_x < decimal_y:
    print('<')
elif decimal_x > decimal_y:
    print('>')
else:
    print('=')