def replace_spaces(s: str) -> str:
    s = s.replace(' ', '_')
    s = s.replace('_', ' ')
    s = s.replace(' ', '_')
    return s
