def func_1(digits, base):
    result = 0
    for digit in digits:
        result = result * base + digit
    return result
(n, bx) = map(int, input().split())
x_digits = list(map(int, input().split()))
(m, by) = map(int, input().split())
y_digits = list(map(int, input().split()))
x = func_1(x_digits, bx)
y = func_1(y_digits, by)
if x < y:
    print('<')
elif x > y:
    print('>')
else:
    print('=')