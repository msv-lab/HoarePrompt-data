t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    z = 0
    for i in range(n):
        if a[a[i] - 1] == i + 1:
            z = 1
            break
    if z == 0:
        print(3)
    else:
        print(2)