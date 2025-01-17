def tetrahedral_number(n: int) -> int:
    """
    This function calculates the nth tetrahedral number.
    
    Parameters:
    n (int): The position of the tetrahedral number to be calculated.
    
    Returns:
    int: The nth tetrahedral number.
    """
    return n * (n + 1) * (n + 2) // 6
