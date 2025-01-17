def max_sum_increasing_subseq(arr, n, i, k):
    # Create a dp array to store the maximum sum of increasing subsequences
    dp = [0] * n
    
    # Initialize dp array with the values of the array itself
    for idx in range(n):
        dp[idx] = arr[idx]
    
    # Fill dp array by finding the maximum sum of increasing subsequences
    for idx in range(1, n):
        for j in range(idx):
            if arr[idx] > arr[j]:
                dp[idx] = max(dp[idx], dp[j] + arr[idx])
    
    # Find the maximum value in dp array up to the i-th index
    max_sum = 0
    for idx in range(i + 1):
        max_sum = max(max_sum, dp[idx])
    
    # Add the value of the k-th element to the maximum sum found
    max_sum += arr[k]
    
    return max_sum

# Tests
assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 2, 5) == 7
assert max_sum_increasing_subseq([11, 15, 19, 21, 26, 28, 31], 7, 2, 4) == 71
