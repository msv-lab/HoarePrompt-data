def max_sub_array_sum_repeated(arr, n, k):
    """
    Find the largest sum of a contiguous array in the modified array 
    which is formed by repeating the given array k times.

    Args:
        arr (list): The input array.
        n (int): The size of the input array.
        k (int): The number of times the array is repeated.

    Returns:
        int: The maximum sum of a contiguous subarray.
    """
    # Calculate the sum of the original array
    total_sum = sum(arr)
    
    # Calculate the maximum sum of a contiguous subarray in the original array
    max_sum = float('-inf')
    current_sum = 0
    for i in range(n):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    
    # If k is 1, return the maximum sum of a contiguous subarray in the original array
    if k == 1:
        return max_sum
    
    # Calculate the maximum sum of a contiguous subarray in the modified array
    max_sum_repeated = max_sum * k
    if total_sum > 0:
        max_sum_repeated += (k - 1) * total_sum
    
    return max_sum_repeated
