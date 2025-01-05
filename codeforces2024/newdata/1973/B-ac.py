for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    k = 1
    for i in range(20):
        prev = -1
        for j, x in enumerate(a):
            if x>>i&1 == 1:
                k = max(k, j - prev)
                prev = j
        if prev != -1:
            k = max(k, n - prev)
    print(k)