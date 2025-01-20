def func_1(s):
    return ''.join([s[i] for i in range(len(s)) if i % 2 != 0])
assert func_1('python') == 'yhn'
assert func_1('program') == 'rga'
assert func_1('language') == 'agae'