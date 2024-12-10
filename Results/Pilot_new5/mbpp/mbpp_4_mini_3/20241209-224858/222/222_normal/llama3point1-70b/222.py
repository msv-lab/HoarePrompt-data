def remove_lowercase(s):
    result = ''
    for char in s:
        if char.isupper():
            result += char
    return result
