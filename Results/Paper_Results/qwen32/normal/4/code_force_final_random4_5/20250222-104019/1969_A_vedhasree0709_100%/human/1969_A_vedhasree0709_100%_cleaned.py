for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    i = 0
    j = 0
    while i <= n - 1:
        p = l[i]
        q = l[p - 1]
        if q == i + 1:
            print(2)
            j = 1
            break
        i += 1
    if j == 0:
        print(3)