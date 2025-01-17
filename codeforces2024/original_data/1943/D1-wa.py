def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    idx = 1
    results = []
    
    for _ in range(t):
        n, k, p = map(int, data[idx:idx + 3])
        idx += 3
        
        # DP array
        max_sum = n * k
        dp = [0] * (max_sum + 1)
        dp[0] = 1
        
        for _ in range(n):
            # Build cumulative sums for optimization
            cumsum = [0] * (max_sum + 2)
            for s in range(max_sum + 1):
                cumsum[s + 1] = (cumsum[s] + dp[s]) % p
            
            # Update DP for the next length
            for s in range(max_sum + 1):
                dp[s] = (cumsum[s + 1] - cumsum[max(0, s - k)]) % p
        
        # Total good arrays
        results.append(sum(dp) % p)
    
    # Print results for all test cases
    sys.stdout.write("\n".join(map(str, results)) + "\n")
