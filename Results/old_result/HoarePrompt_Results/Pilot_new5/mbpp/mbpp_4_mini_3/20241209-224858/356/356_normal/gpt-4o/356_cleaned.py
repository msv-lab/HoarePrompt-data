def func_1(s):
    return s.replace(' ', '')
assert func_1('python  program') == 'pythonprogram'
assert func_1('python   programming    language') == 'pythonprogramminglanguage'
assert func_1('python                     program') == 'pythonprogram'
assert func_1('   python                     program') == 'pythonprogram'