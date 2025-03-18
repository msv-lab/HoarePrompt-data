def func_1(a, b):
    return abs(a * b) // gcd(a, b)

def func_2(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = func_1(result, num)
    return result
t = int(input())
for _ in range(t):
    n = int(input())
    k = list(map(int, input().split()))
    m = func_2(k)
    c = []
    for i in range(n):
        c.append(m // k[i])
    if sum(c) >= m:
        print(-1)
        continue
    for i in range(n):
        print(c[i], end=' ')
    print('\n', end='')