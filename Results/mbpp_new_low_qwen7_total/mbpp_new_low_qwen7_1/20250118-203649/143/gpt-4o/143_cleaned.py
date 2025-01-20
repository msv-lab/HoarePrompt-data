def func_1(text):
    pattern = 'a(b{2,3})'
    match = re.search(pattern, text)
    return bool(match)
assert func_1('ac') == False
assert func_1('dc') == False
assert func_1('abbbba') == True