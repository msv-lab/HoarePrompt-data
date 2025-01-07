def func_1(snake_str):
    components = snake_str.split('_')
    return ''.join((x.capitalize() for x in components))
assert func_1('python_program') == 'PythonProgram'
assert func_1('python_language') == 'PythonLanguage'
assert func_1('programming_language') == 'ProgrammingLanguage'