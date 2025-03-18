def func_1(n):
    dp = [1, 1]
    for i in range(2, n + 1):
        dp += [(dp[-1] + 2 * (i - 1) * dp[-2]) % (7 + 10 ** 9)]
        dp.pop(0)
    return dp[-1]
t = int(input())
for _ in range(t):
    L = list(map(int, input().split()))
    (n, k) = (L[0], L[1])
    for j in range(k):
        L1 = list(map(int, input().split()))
        (a, b) = (L1[0], L1[1])
        if a != b:
            n -= 2
        else:
            n -= 1
    print(func_1(n))
    continue