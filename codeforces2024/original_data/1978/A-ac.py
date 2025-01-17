for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    mx = 0
    for i in range(n - 1):
        mx = max(mx, a[i])
    print(mx + a[n - 1])

