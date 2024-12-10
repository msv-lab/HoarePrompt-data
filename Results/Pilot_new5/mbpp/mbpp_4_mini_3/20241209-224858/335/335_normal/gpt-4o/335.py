def occurance_substring(main_string, sub_string):
    start_pos = main_string.find(sub_string)
    if start_pos == -1:
        return None
    end_pos = start_pos + len(sub_string)
    return (sub_string, start_pos, end_pos)

# Test cases
assert occurance_substring('python programming, python language', 'python') == ('python', 0, 6)
assert occurance_substring('python programming,programming language', 'programming') == ('programming', 7, 18)
assert occurance_substring('python programming,programming language', 'language') == ('language', 31, 39)
assert occurance_substring('c++ programming, c++ language', 'python') == None
