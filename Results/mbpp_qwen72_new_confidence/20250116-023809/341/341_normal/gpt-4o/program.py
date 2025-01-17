def odd_length_sum(arr):
    total_sum = 0
    n = len(arr)
    
    for start in range(n):
        for length in range(1, n-start+1, 2):  # Only odd lengths
            subarray = arr[start:start+length]
            total_sum += sum(subarray)
    
    return total_sum
