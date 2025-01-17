def solve_puzzle(c1, c2, c3, c4):
    MOD = 998244353
    
    # Dynamic programming table to store the number of ways to arrange elements
    dp = [[0 for _ in range(4)] for _ in range(max(c1, c2, c3, c4) + 1)]
    
    # Base case: There is exactly one way to have zero elements of each type
    dp[0][0] = 1
    
    # Fill the dynamic programming table
    for i in range(1, max(c1, c2, c3, c4) + 1):
        # Update the number of ways for each type of element
        if i <= c1:
            dp[i][0] = (dp[i-1][1] + dp[i-1][2] + dp[i-1][3]) % MOD
        if i <= c2:
            dp[i][1] = (dp[i-1][0] + dp[i-1][2] + dp[i-1][3]) % MOD
        if i <= c3:
            dp[i][2] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][3]) % MOD
        if i <= c4:
            dp[i][3] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % MOD
    
    # The total number of ways to arrange all elements is the sum of the last row
    total_ways = sum(dp[max(c1, c2, c3, c4)]) % MOD
    return total_ways

# Main function to handle input and output
def main():
    MOD = 998244353
    t = int(input())
    results = []
    
    for _ in range(t):
        c1, c2, c3, c4 = map(int, input().split())
        result = solve_puzzle(c1, c2, c3, c4)
        results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()