n = int(input())
a = list(map(int, input().split()))

def count_good_subsequences(n, a):
    MOD = 998244353
    dp = [0] * (n+1)
    dp[0] = 0
    
    for i in range(1, n+1):
        dp[i] = 1
        for j in range(i-2, -1, -1):
            if a[i-1] > a[j] or a[i-1] == -1:
                dp[i] = (dp[i] + dp[j]) % MOD
    
    return dp[n] - 1

result = count_good_subsequences(n, a)
print(result)