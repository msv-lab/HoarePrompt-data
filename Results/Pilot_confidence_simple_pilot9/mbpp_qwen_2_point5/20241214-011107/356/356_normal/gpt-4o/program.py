def remove_all_spaces(s):
    return s.replace(" ", "")

# Test cases
assert remove_all_spaces('python  program') == 'pythonprogram'
assert remove_all_spaces('python   programming    language') == 'pythonprogramminglanguage'
assert remove_all_spaces('python                     program') == 'pythonprogram'
assert remove_all_spaces('   python                     program') == 'pythonprogram'
