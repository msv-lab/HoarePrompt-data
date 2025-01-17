def centered_hexagonal_number(n: int) -> int:
    """
    This function calculates the nth centered hexagonal number.
    
    Args:
    n (int): The position of the centered hexagonal number to be calculated.
    
    Returns:
    int: The nth centered hexagonal number.
    """
    return n * (2 * n - 1)
