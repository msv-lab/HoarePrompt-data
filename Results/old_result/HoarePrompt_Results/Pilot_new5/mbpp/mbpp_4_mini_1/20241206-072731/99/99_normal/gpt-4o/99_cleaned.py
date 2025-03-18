def func_1(s):
    return ''.join([s[i] for i in range(len(s)) if i % 2 == 0])
assert func_1('abcdef') == 'ace'
assert func_1('python') == 'pto'
assert func_1('data') == 'dt'
assert func_1('lambs') == 'lms'