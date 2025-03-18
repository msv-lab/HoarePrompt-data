from math import gcd

t = int(input())
for _ in range(t):
    n = int(input())
    k = list(map(int, input().split()))
    m = 1
    for i in range(n):
        m = m * k[i]
    c = []
    for i in range(n):
        c.append(int(m / k[i]))
    hcf = func_1(c)
    for i in range(n):
        c[i] = int(c[i] / hcf)
    if sum(c) >= m:
        print(-1)
    else:
        for i in range(n):
            print(c[i], end=' ')
        print('')

def func_1(numbers):
    hcf = numbers[0]
    for num in numbers[1:]:
        hcf = gcd(hcf, num)
    return hcf

