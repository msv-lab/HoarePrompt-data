def calculate_trail_combinations(m, n, s, l):
    MOD = 10**9 + 7
    
    # Initialize dp array
    dp = [[0] * (n + 1) for _ in range(m)]
    
    # Base case: On day 1, Harry starts from cabin 1
    dp[0][1] = sum(s[i] > 0 for i in range(m)) % MOD
    
    # Fill the dp array
    for day in range(2, n + 1):
        for i in range(m):
            if s[i] > 0:
                dp[i][day] += (dp[(i - 1) % m][day - 1] * l[i]) % MOD
                dp[i][day] %= MOD
            if l[i] > 0:
                dp[i][day] += (dp[(i + 1) % m][day - 1] * s[i]) % MOD
                dp[i][day] %= MOD
    
    # Sum up all possible combinations for reaching any cabin on the last day
    result = sum(dp[i][n] for i in range(m)) % MOD
    
    return result

# Input reading
m, n = map(int, input().split())
s = list(map(int, input().split()))
l = list(map(int, input().split()))

# Calculate and print the result
result = calculate_trail_combinations(m, n, s, l)
print(result)