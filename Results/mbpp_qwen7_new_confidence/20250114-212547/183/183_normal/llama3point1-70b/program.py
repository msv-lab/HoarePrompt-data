def count_element_in_list(lst, element):
    """
    Counts the number of sublists containing a particular element.

    Args:
        lst (list): The list of sublists to search.
        element: The element to count.

    Returns:
        int: The number of sublists containing the element.
    """
    return sum(1 for sublist in lst if element in sublist)
