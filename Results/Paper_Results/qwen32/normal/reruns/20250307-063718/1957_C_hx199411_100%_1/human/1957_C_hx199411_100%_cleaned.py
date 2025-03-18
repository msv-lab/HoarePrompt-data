t = int(input())
while t:
    t -= 1
    (n, k) = list(map(int, input().split(' ')))
    num = 0
    for i in range(k):
        (c, r) = list(map(int, input().split(' ')))
        if c == r:
            num += 1
        else:
            num += 2
    m = n - num
    if m == 0:
        print(1)
    elif m == 1:
        print(1)
    else:
        dp = [0 for i in range(m + 1)]
        dp[1] = 1
        dp[2] = 3
        for i in range(3, m + 1):
            dp[i] = (dp[i - 1] + (i - 1) * dp[i - 2] * 2) % (10 ** 9 + 7)
        print(dp[m])