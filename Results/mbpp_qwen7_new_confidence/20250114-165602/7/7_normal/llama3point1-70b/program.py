def find_Rotations(s: str) -> int:
    """
    Find the minimum number of rotations required to get the same string.
    
    Args:
        s (str): The input string.
    
    Returns:
        int: The minimum number of rotations required.
    """
    n = len(s)
    for i in range(1, n):
        if s[i:] + s[:i] == s:
            return i
    return n
