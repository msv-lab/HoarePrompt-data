def max_sub_array_sum(nums, n):
    """
    Find the sum of the largest contiguous sublist in the given list.

    Args:
        nums (list): The input list of numbers.
        n (int): The size of the input list.

    Returns:
        int: The sum of the largest contiguous sublist.
    """
    if not nums:
        return 0

    max_sum = float('-inf')
    current_sum = 0

    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum
