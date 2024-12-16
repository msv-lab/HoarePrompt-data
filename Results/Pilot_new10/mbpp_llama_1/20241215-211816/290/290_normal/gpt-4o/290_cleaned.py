def func_1(s):
    if 'z' in s[1:-1]:
        return True
    return False
assert func_1('pythonzabc.') == True
assert func_1('zxyabc.') == False
assert func_1('  lang  .') == False