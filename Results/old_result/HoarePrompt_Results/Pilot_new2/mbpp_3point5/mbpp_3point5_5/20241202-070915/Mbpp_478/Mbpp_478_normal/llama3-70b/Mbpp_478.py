def remove_lowercase(s: str) -> str:
    return ''.join(c for c in s if c.isupper())
