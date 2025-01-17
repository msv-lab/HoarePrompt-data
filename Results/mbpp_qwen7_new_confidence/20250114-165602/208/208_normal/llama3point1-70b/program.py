def remove_uppercase(s: str) -> str:
    result = ''
    substring = ''
    for char in s:
        if char.isupper():
            substring += char
        else:
            result += char
            substring = ''
    return result
