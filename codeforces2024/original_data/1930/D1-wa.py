def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    num_cases = int(data[index])
    index += 1
    results = []
    
    for _ in range(num_cases):
        n = int(data[index])
        index += 1
        s = data[index]
        index += 1
        
        # Initialize the DP array
        dp = [0] * (n + 1)
        result = 0
        
        # Traverse the string from the end to the beginning
        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                # If the current character is '1', calculate the contribution
                dp[i] = n - i + dp[i + 1]
            else:
                # If the current character is '0', carry forward the previous value
                dp[i] = dp[i + 1]
        
        # Sum up all the values in the DP array
        result = sum(dp[:n])
        
        # Store the result for the current test case
        results.append(result)
    
    # Output all results
    for res in results:
        print(res)

if __name__ == "__main__":
    solve()