# Include necessary imports if any
import io
import sys

def run_program_with_captured_io(input_data):
    original_stdin = sys.stdin
    original_stdout = sys.stdout

    try:
        sys.stdin = io.StringIO(input_data)
        captured_output = io.StringIO()
        sys.stdout = captured_output

        with open("program.py", "r", encoding="utf-8") as f:
            code = f.read()
            exec(code, {})

        return captured_output.getvalue().strip()
    
    finally:
        sys.stdin = original_stdin
        sys.stdout = original_stdout

# Write your test cases below
# Each test case should include assertions based on the problem description

# Test case 1: From the example
input_data = """3
sinktheyacht
lllllllll
uwuowouwu"""
expected_output = """YES
1
sinktheyacht
NO
YES
3
uw uow ouwu"""
assert run_program_with_captured_io(input_data) == expected_output

# Test case 2: Single character string
input_data = """1
a"""
expected_output = """NO"""
assert run_program_with_captured_io(input_data) == expected_output

# Test case 3: Two character non-palindrome
input_data = """1
ab"""
expected_output = """YES
1
ab"""
assert run_program_with_captured_io(input_data) == expected_output

# Test case 4: Two character palindrome
input_data = """1
aa"""
expected_output = """NO"""
assert run_program_with_captured_io(input_data) == expected_output

# Test case 5: Longer palindrome
input_data = """1
racecar"""
expected_output = """NO"""
assert run_program_with_captured_io(input_data) == expected_output

# Test case 6: Longer non-palindrome
input_data = """1
abcdefg"""
expected_output = """YES
1
abcdefg"""
assert run_program_with_captured_io(input_data) == expected_output

# Test case 7: Repeated pattern non-palindrome
input_data = """1
abcabcabc"""
expected_output = """YES
3
abc abc abc"""
assert run_program_with_captured_io(input_data) == expected_output

# Test case 8: Repeated pattern palindrome
input_data = """1
abababa"""
expected_output = """NO"""
assert run_program_with_captured_io(input_data) == expected_output

# Test case 9: Mixed patterns
input_data = """2
abacaba
abcde"""
expected_output = """NO
YES
1
abcde"""
assert run_program_with_captured_io(input_data) == expected_output

# Test case 10: Large input with multiple test cases
input_data = """5
a
aa
aaa
aaaa
abcde"""
expected_output = """NO
NO
NO
NO
YES
1
abcde"""
assert run_program_with_captured_io(input_data) == expected_output

# End of script