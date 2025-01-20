def func_1(x):
    return x & x + 1 == 0

def func_2(x):
    operations = []
    count = 0
    while not func_1(x) and count < 40:
        if count % 2 == 0:
            n = 0
            while (1 << n) - 1 <= x:
                n += 1
            while n > 0 and x >> n - 1 & 1 == 1:
                n -= 1
            if n == 0:
                break
            operations.append(n)
            x ^= (1 << n) - 1
        else:
            x += 1
        count += 1
    return (count, operations)
x = int(input())
(t, ops) = func_2(x)
print(t)
for i in range(0, len(ops), 2):
    print(ops[i], end=' ')