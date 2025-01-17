n = int(input())

if n == 1 or n == 2:
    print(-1)
else:
    if n % 2 == 1:
        m = (n * n - 1) // 2
        k = (n * n + 1) // 2
    else:
        m = (n * n // 4) - 1
        k = (n * n // 4) + 1
    print(m, k)
