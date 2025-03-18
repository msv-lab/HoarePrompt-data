def func_1(s):
    result = ''
    for char in s:
        if char.isupper():
            result += char
    return result