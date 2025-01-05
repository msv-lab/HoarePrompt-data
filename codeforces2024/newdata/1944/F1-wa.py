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
        k = int(data[index])
        index += 1
        p = int(data[index])
        index += 1
        
        # Since every integer from 1 to n occurs exactly twice in a,
        # and we need to find the number of good arrays of length n
        # such that 0 <= a_i <= k for all 1 <= i <= n,
        # we can use dynamic programming to solve this problem.
        
        # dp[x] will be the number of ways to form an array of length x
        # such that all elements can be made zero with the operation.
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: one way to have an empty array
        
        # We need to count all arrays of length n where the maximum element is <= k
        # and can be reduced to zero.
        # Since every element from 1 to n appears exactly twice, we can consider pairs.
        
        # We iterate over all possible lengths of the array we can form
        for length in range(1, n + 1):
            # We iterate over all values that can be included in the array
            for value in range(1, min(k, length) + 1):
                if length >= 2 * value:
                    # We can include the pair (value, value) in our array
                    dp[length] = (dp[length] + dp[length - 2 * value]) % p
        
        # The result for this test case is the sum of dp[x] for all x from 1 to n
        result = sum(dp[1:n+1]) % p
        results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()