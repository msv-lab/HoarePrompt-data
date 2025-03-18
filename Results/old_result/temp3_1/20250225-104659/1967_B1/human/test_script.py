import math

def count_valid_pairs(n, m):
    def gcd(x, y):
        while y != 0:
            (x, y) = (y, x % y)
        return x
    
    ans = 0
    for a in range(1, n + 1):
        for b in range(1, m + 1):
            if (a + b) % (b * gcd(a, b)) == 0:
                ans += 1
    return ans

def run_program_with_captured_io(input_data):
    import io
    import sys

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

# Test the correct function with assertions
assert count_valid_pairs(1, 1) == 1
assert count_valid_pairs(2, 3) == 3
assert count_valid_pairs(3, 5) == 4
assert count_valid_pairs(10, 8) == 14
assert count_valid_pairs(100, 1233) == 153
assert count_valid_pairs(1000000, 1145141) == 1643498

# Test the provided program script with assertions
input_data = """6\n1 1\n2 3\n3 5\n10 8\n100 1233\n1000000 1145141"""
expected_output = "1\n3\n4\n14\n153\n1643498"
assert run_program_with_captured_io(input_data) == expected_output

print("All tests passed!")