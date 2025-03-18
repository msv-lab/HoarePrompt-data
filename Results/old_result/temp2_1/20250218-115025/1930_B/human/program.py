def func():
    for _ in range(int(input())):
        n = int(input())
        a = list(range(1, n + 1))
        for i in range(n // 2):
            a[2 * i + 1] = n - i
            a[2 * i] = i + 1
        if len(a) % 2 == 1:
            a[n - 1] = n // 2 + 1
        print(*a)

