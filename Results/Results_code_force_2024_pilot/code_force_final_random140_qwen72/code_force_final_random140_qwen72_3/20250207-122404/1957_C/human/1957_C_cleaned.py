def func_1(x):
    dp = {}

    def helper(len):
        if len <= 0:
            return 1
        if len in dp:
            return dp[len]
        x1 = helper(len - 1)
        x2 = 2 * (len - 1) * helper(len - 2)
        y = x1 + x2
        dp[len] = y
        return y
    return helper(x)
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