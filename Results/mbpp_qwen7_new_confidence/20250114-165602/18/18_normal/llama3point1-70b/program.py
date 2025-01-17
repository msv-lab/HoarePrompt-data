def opposite_Signs(a: int, b: int) -> bool:
    """
    Checks whether two integers have opposite signs.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        bool: True if the integers have opposite signs, False otherwise.
    """
    return (a < 0 and b > 0) or (a > 0 and b < 0)
