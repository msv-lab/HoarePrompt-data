# Include necessary imports if any
# Assume the provided program is saved as 'program.py' and can be imported from the same dir.

from program import *

# Write your test cases below
# Each test case should include assertions based on the problem description
# Example:

# Test Case 1: n = 4
def test_case_1():
    from io import StringIO
    import sys
    sys.stdin = StringIO("2\n4\n")
    result = []
    original_print = print
    def mock_print(*args):
        result.extend(args)
    print = mock_print
    func()
    print = original_print
    assert result == ['4 1 2 3 '], f"Expected ['4 1 2 3 '], got {result}"

# Test Case 2: n = 3
def test_case_2():
    from io import StringIO
    import sys
    sys.stdin = StringIO("2\n3\n")
    result = []
    original_print = print
    def mock_print(*args):
        result.extend(args)
    print = mock_print
    func()
    print = original_print
    assert result == ['1 2 3 '], f"Expected ['1 2 3 '], got {result}"

# Test Case 3: n = 5
def test_case_3():
    from io import StringIO
    import sys
    sys.stdin = StringIO("1\n5\n")
    result = []
    original_print = print
    def mock_print(*args):
        result.extend(args)
    print = mock_print
    func()
    print = original_print
    assert result == ['1 3 2 4 5 '], f"Expected ['1 3 2 4 5 '], got {result}"

# Test Case 4: n = 10
def test_case_4():
    from io import StringIO
    import sys
    sys.stdin = StringIO("1\n10\n")
    result = []
    original_print = print
    def mock_print(*args):
        result.extend(args)
    print = mock_print
    func()
    print = original_print
    expected_output = "1 3 2 5 4 7 6 9 8 10\n"
    assert result == expected_output.split(), f"Expected {expected_output.strip()}, got {result}"

# Run all test cases
test_case_1()
test_case_2()
test_case_3()
test_case_4()

# End of script