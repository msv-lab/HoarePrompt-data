def text_lowercase_underscore(s: str) -> bool:
    """
    Returns True if the input string contains sequences of lowercase letters joined with an underscore, False otherwise.
    """
    return all(c.islower() or c == '_' for c in s)
