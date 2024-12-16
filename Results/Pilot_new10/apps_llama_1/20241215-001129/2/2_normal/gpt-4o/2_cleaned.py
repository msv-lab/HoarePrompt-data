def func_1(n):
    return sum((int(digit) for digit in str(n)))
x = int(input().strip())
x_str = str(x)
n = len(x_str)
if x_str[0] != '1':
    candidate = int(x_str[0]) - 1
    candidate = str(candidate) + '9' * (n - 1)
else:
    candidate = '9' * (n - 1)
candidate = int(candidate)
sum_x = func_1(x)
sum_candidate = func_1(candidate)
if sum_candidate > sum_x:
    print(candidate)
else:
    print(x)