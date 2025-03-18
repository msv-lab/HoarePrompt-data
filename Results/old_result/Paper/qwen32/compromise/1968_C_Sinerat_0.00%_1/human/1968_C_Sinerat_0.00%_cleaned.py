for _ in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    a = [0] * n
    a[0] = 500
    for i in range(1, n):
        a[i] = a[i - 1] + x[i - 1]
    print(*a)