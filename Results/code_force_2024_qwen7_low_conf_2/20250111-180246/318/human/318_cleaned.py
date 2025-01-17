t = int(input())
for _ in range(t):
    n = int(input())
    mid = n // 2
    a = []
    for i in range(1, n // 2 + 1):
        a.append(i)
        a.append(mid + i)
    if n % 2 != 0:
        a.append(n)
    for i in range(n):
        print(a[i], end=' ')
    print('\n', end='')