mod = 998244353

# Precompute factorials and their modular inverses
fact = [1] * 5005
rfact = [1] * 5005

# Calculate factorials and their inverses using Fermat's Little Theorem
for i in range(1, 5005):
    fact[i] = fact[i - 1] * i % mod
    rfact[i] = pow(fact[i], mod - 2, mod)

# Function to calculate combinations C(n, r) = n! / (r! * (n-r)!)
def C(n, r):
    if n < r or r < 0:
        return 0
    return fact[n] * rfact[r] * rfact[n - r] % mod

# Read number of test cases
t = int(input())
for _ in range(t):
    # Read size of array and the sorted prefix sum array
    n = int(input())
    arr = list(map(int, input().split())) + [0]
    arr.sort()
    m, M = arr[0], arr[-1]
    flag = 0
    
    # Check for invalid configurations
    for i in range(n - 1):
        if arr[i + 1] - arr[i] > 1:
            flag = 1
            break
    
    # If invalid, output 0
    if flag == 1 or m * M > 0:
        print(0)
    else:
        # Count occurrences of each prefix sum
        cnt = [0] * 10005
        for i in arr:
            cnt[i] += 1
        
        # Initialize DP table
        dp = [[[0, 0] for _ in range(cnt[i + m] + 1)] for i in range(M - m + 1)]
        dp[0][cnt[m] - 1][0] = 1
        
        # Fill DP table
        for i in range(1, M - m + 1):
            p = i + m
            for j in range(cnt[p] + 1):
                for j2 in range(cnt[p - 1] + 1):
                    if p <= 0:
                        hole = cnt[p] - j
                        if hole == j2 + 2:
                            dp[i][j][0] = (dp[i][j][0] + dp[i - 1][j2][0] * C(cnt[p] - 1, hole - 1)) % mod
                        if hole == j2 + 1:
                            dp[i][j][1] = (dp[i][j][1] + dp[i - 1][j2][0] * C(cnt[p] - 1, hole - 1) +
                                           dp[i - 1][j2][1] * C(cnt[p] - 1, hole - 1)) % mod
                    else:
                        hole = cnt[p] - j
                        if hole == j2 + 1:
                            dp[i][j][0] = (dp[i][j][0] + dp[i - 1][j2][0] * C(cnt[p] - 1, hole - 1)) % mod
                        if hole == j2:
                            dp[i][j][1] = (dp[i][j][1] + dp[i - 1][j2][0] * C(cnt[p] - 1, hole - 1) +
                                           dp[i - 1][j2][1] * C(cnt[p] - 1, hole - 1)) % mod
        
        # Calculate the final answer from the DP table
        ans = sum(dp[-1][0]) % mod
        print(ans)