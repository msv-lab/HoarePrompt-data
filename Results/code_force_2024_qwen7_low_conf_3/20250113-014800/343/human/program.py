def find_missing_sum(n, subarray_sums):
    # Calculate the total number of subarrays
    total_subarrays = n * (n + 1) // 2
    
    # Calculate the expected sum of all subarray sums
    # This is the sum of the first n natural numbers squared
    expected_sum = sum(range(1, n + 1)) ** 2
    
    # Calculate the actual sum of the given subarray sums
    actual_sum = sum(subarray_sums)
    
    # The missing sum is the difference
    missing_sum = expected_sum - actual_sum
    
    return missing_sum

def reconstruct_palindrome(n, subarray_sums, missing_sum):
    # Sort the subarray sums
    subarray_sums.sort()
    
    # Initialize the palindrome array
    a = [0] * n
    
    # Use the missing sum to help reconstruct the array
    # This is a simplified approach, and may need adjustments
    # based on the specific problem constraints and examples.
    
    # For simplicity, let's assume the missing sum is the sum of the middle element
    # This is a naive assumption and may not hold for all cases.
    # A more robust solution would involve more complex logic.
    
    # Set the middle element
    mid = n // 2
    a[mid] = missing_sum // (mid + 1)
    
    # Fill the rest of the array symmetrically
    for i in range(mid):
        a[i] = subarray_sums[i] - a[mid]
        a[n - 1 - i] = a[i]
    
    return a

def solve():
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
        subarray_sums = list(map(int, data[index:index + (n * (n + 1) // 2) - 1]))
        index += (n * (n + 1) // 2) - 1
        
        missing_sum = find_missing_sum(n, subarray_sums)
        palindrome = reconstruct_palindrome(n, subarray_sums, missing_sum)
        
        results.append(' '.join(map(str, palindrome)))
    
    for result in results:
        print(result)