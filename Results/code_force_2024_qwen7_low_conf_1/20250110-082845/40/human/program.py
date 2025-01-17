MOD = 998244353

def count_valid_arrays(n, p):
    # dp[i][j] will store the number of ways to achieve prefix sum j using first i elements
    dp = [0] * (2 * n + 1)
    offset = n  # To handle negative indices, we use an offset
    dp[offset] = 1  # Base case: one way to have prefix sum 0 with 0 elements
    
    for i in range(1, n + 1):
        new_dp = [0] * (2 * n + 1)
        for j in range(2 * n + 1):
            if dp[j] > 0:
                # If we can achieve prefix sum j-offset with i-1 elements
                # We can achieve j-offset+1 with i elements by adding 1
                if j + 1 <= 2 * n:
                    new_dp[j + 1] = (new_dp[j + 1] + dp[j]) % MOD
                # We can achieve j-offset-1 with i elements by adding -1
                if j - 1 >= 0:
                    new_dp[j - 1] = (new_dp[j - 1] + dp[j]) % MOD
        dp = new_dp
    
    # We need to count the number of ways to achieve the final prefix sum p_n
    # which is p[-1] in the sorted array
    final_sum = p[-1] + offset
    return dp[final_sum]

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        p = list(map(int, data[index:index + n]))
        index += n
        
        result = count_valid_arrays(n, p)
        results.append(result)
    
    for res in results:
        print(res)

if __name__ == "__main__":
    main()