def findKthLargest(n, m, k):
    def count_less_equal(x):
        count = 0
        for i in range(1, n + 1):
            count += min(x // i, m)
        return count
    
    low, high = 1, n * m
    while low < high:
        mid = (low + high) // 2
        if count_less_equal(mid) < k:
            low = mid + 1
        else:
            high = mid
    return low

# Read input
n, m, k = map(int, input().strip().split())

# Find and print the k-th largest number in the n x m multiplication table
print(findKthLargest(n, m, k))
