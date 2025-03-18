t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    max = 0
    for i in range(1, n):
        if min(a[i], a[i - 1]) > max:
            max = min(a[i], a[i - 1])
    print(max)