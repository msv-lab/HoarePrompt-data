def func_1(x):
    if x <= 1:
        return False
    if x <= 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True
n = int(input())
for m in range(1, 1001):
    if not func_1(n * m + 1):
        print(m)
        break