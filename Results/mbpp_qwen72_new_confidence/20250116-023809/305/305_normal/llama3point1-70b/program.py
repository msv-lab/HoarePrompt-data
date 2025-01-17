def left_insertion(sorted_list, value):
    """
    Locate the left insertion point for a specified value in sorted order.

    Args:
        sorted_list (list): A sorted list of elements.
        value: The value to be inserted.

    Returns:
        int: The index where the value should be inserted to maintain sorted order.
    """
    for i, x in enumerate(sorted_list):
        if x >= value:
            return i
    return len(sorted_list)
