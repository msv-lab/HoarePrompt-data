import sys
input = sys.stdin.read

def solve():
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n, m = int(data[idx]), int(data[idx + 1])
        idx += 2
        a = list(map(int, data[idx:idx + n]))
        idx += n
        b = list(map(int, data[idx:idx + m]))
        idx += m
        
        # Apply the transformation to a using b
        for i in range(n):
            a[i] = b[a[i] - 1]
        
        # Now we need to check if we can make a non-decreasing
        # and calculate the minimum number of tricks.
        
        # dp[i] will store the length of the longest non-decreasing subsequence
        # ending with the value i.
        dp = [0] * (m + 1)
        
        for x in a:
            # We update dp[x] based on the maximum dp value for all values <= x
            max_len = 0
            for i in range(x + 1):
                max_len = max(max_len, dp[i])
            dp[x] = max_len + 1
        
        # The length of the longest non-decreasing subsequence
        longest_non_decreasing = max(dp)
        
        # The minimum number of tricks is the difference between n and the length
        # of the longest non-decreasing subsequence.
        results.append(str(n - longest_non_decreasing))
    
    sys.stdout.write("\n".join(results) + "\n")

# Run the solution
solve()