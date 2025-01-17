def max_sum(arr):
    n = len(arr)
    
    if n == 0:
        return 0
    
    # Step 1: Calculate MSIS for each element
    msis = [0] * n
    for i in range(n):
        msis[i] = arr[i]
        for j in range(i):
            if arr[j] < arr[i] and msis[i] < msis[j] + arr[i]:
                msis[i] = msis[j] + arr[i]
    
    # Step 2: Calculate MSDS for each element
    msds = [0] * n
    for i in range(n-1, -1, -1):
        msds[i] = arr[i]
        for j in range(n-1, i, -1):
            if arr[j] < arr[i] and msds[i] < msds[j] + arr[i]:
                msds[i] = msds[j] + arr[i]
    
    # Step 3: Combine MSIS and MSDS to get the maximum sum bitonic subsequence
    max_bitonic_sum = 0
    for i in range(n):
        max_bitonic_sum = max(max_bitonic_sum, msis[i] + msds[i] - arr[i])
    
    return max_bitonic_sum

# Tests
assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
assert max_sum([80, 60, 30, 40, 20, 10]) == 210
assert max_sum([2, 3, 14, 16, 21, 23, 29, 30]) == 138
