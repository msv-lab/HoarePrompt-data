def func_1(s):
    if not s:
        return True
    first_char = s[0]
    for char in s:
        if char != first_char:
            return False
    return True
assert func_1('python') == False
assert func_1('aaa') == True
assert func_1('data') == False