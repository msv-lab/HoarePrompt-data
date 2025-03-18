def func_1(input_string):
    return input_string.replace(' ', '%20')
assert func_1('My Name is Dawood') == 'My%20Name%20is%20Dawood'
assert func_1('I am a Programmer') == 'I%20am%20a%20Programmer'
assert func_1('I love Coding') == 'I%20love%20Coding'