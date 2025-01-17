def max_val(lst):
    """
    This function finds the maximum value in a given heterogeneous list.
    
    Args:
        lst (list): A list containing different types of elements.
    
    Returns:
        The maximum value from the list.
    """
    max_val = float('-inf')  # Initialize max_val as negative infinity
    for item in lst:
        if isinstance(item, (int, float)):  # Check if the item is a number
            max_val = max(max_val, item)  # Update max_val if the item is larger
    return max_val
