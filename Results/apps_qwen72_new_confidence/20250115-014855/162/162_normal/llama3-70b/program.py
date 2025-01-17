x = int(input())
m = 0
while (1 << m) - 1 < x:
    m += 1
t = 0
operations = []
while x != (1 << m) - 1:
    n = m
    while (x ^ ((1 << n) - 1)) != (1 << m) - 1:
        n -= 1
    x ^= (1 << n) - 1
    operations.append(n)
    x += 1
    t += 2
print(t)
for i in range(0, t, 2):
    print(operations[i])
