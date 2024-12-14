def func_1(main_string, sub_string):
    start_pos = main_string.find(sub_string)
    if start_pos == -1:
        return None
    end_pos = start_pos + len(sub_string)
    return (sub_string, start_pos, end_pos)
assert func_1('python programming, python language', 'python') == ('python', 0, 6)
assert func_1('python programming,programming language', 'programming') == ('programming', 7, 18)
assert func_1('python programming,programming language', 'language') == ('language', 31, 39)
assert func_1('c++ programming, c++ language', 'python') == None