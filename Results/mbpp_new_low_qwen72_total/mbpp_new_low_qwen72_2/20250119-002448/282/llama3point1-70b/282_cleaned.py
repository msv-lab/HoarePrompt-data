def func_1(s: str) -> str:
    s = s.replace(' ', '_')
    s = s.replace('_', ' ')
    s = s.replace(' ', '_')
    return s