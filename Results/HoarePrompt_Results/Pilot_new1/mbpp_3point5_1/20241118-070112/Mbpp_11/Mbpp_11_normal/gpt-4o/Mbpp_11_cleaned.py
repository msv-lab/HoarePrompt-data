def func_1(s: str, ch: str) -> str:
    first_index = s.find(ch)
    last_index = s.rfind(ch)
    if first_index == -1 or last_index == -1 or first_index == last_index:
        return s
    return s[:first_index] + s[first_index + 1:last_index] + s[last_index + 1:]
assert func_1('hello', 'l') == 'heo'
assert func_1('abcda', 'a') == 'bcd'
assert func_1('PHP', 'P') == 'H'