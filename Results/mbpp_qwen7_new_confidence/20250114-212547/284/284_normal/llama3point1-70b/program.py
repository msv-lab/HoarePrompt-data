def pair_xor_Sum(nums, n):
    """
    This function calculates the sum of xor of all pairs of numbers in the given list.
    
    Args:
        nums (list): A list of integers.
        n (int): The number of elements in the list.
    
    Returns:
        int: The sum of xor of all pairs of numbers in the list.
    """
    total_sum = 0
    for i in range(n):
        for j in range(i+1, n):
            total_sum += nums[i] ^ nums[j]
    return total_sum
