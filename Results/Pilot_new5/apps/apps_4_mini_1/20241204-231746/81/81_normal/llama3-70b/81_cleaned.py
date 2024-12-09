def func_1(a, b):
    while b:
        (a, b) = (b, a % b)
    return a

def func_2(a, b):
    return a * b // func_1(a, b)
(l, r, x, y) = map(int, input().split())
count = 0
for a in range(l, r + 1):
    for b in range(a, r + 1):
        if func_1(a, b) == x and func_2(a, b) == y:
            count += 1
print(count)