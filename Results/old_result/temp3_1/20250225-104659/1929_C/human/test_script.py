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

# Test cases
test_cases = [
    (
        "9\n2 1 7\n2 1 1\n2 3 15\n3 3 6\n4 4 5\n5 4 7\n4 88 1000000000\n25 69 231\n13 97 18806",
        "YES\nNO\nYES\nNO\nNO\nYES\nNO\nNO\nNO"
    ),
    (
        "1\n2 1 100",
        "YES"
    ),
    (
        "1\n2 2 1",
        "NO"
    ),
    (
        "1\n3 1 1",
        "NO"
    ),
    (
        "1\n3 2 1",
        "NO"
    ),
    (
        "1\n3 3 1",
        "NO"
    ),
    (
        "1\n4 1 1",
        "NO"
    ),
    (
        "1\n4 2 1",
        "NO"
    ),
    (
        "1\n4 3 1",
        "NO"
    ),
    (
        "1\n4 4 1",
        "NO"
    ),
    (
        "1\n4 5 1",
        "NO"
    ),
    (
        "1\n4 6 1",
        "NO"
    ),
    (
        "1\n4 7 1",
        "NO"
    ),
    (
        "1\n4 8 1",
        "NO"
    ),
    (
        "1\n4 9 1",
        "NO"
    ),
    (
        "1\n4 10 1",
        "NO"
    ),
    (
        "1\n4 11 1",
        "NO"
    ),
    (
        "1\n4 12 1",
        "NO"
    ),
    (
        "1\n4 13 1",
        "NO"
    ),
    (
        "1\n4 14 1",
        "NO"
    ),
    (
        "1\n4 15 1",
        "NO"
    ),
    (
        "1\n4 16 1",
        "NO"
    ),
    (
        "1\n4 17 1",
        "NO"
    ),
    (
        "1\n4 18 1",
        "NO"
    ),
    (
        "1\n4 19 1",
        "NO"
    ),
    (
        "1\n4 20 1",
        "NO"
    ),
    (
        "1\n4 21 1",
        "NO"
    ),
    (
        "1\n4 22 1",
        "NO"
    ),
    (
        "1\n4 23 1",
        "NO"
    ),
    (
        "1\n4 24 1",
        "NO"
    ),
    (
        "1\n4 25 1",
        "NO"
    ),
    (
        "1\n4 26 1",
        "NO"
    ),
    (
        "1\n4 27 1",
        "NO"
    ),
    (
        "1\n4 28 1",
        "NO"
    ),
    (
        "1\n4 29 1",
        "NO"
    ),
    (
        "1\n4 30 1",
        "NO"
    ),
    (
        "1\n4 31 1",
        "NO"
    ),
    (
        "1\n4 32 1",
        "NO"
    ),
    (
        "1\n4 33 1",
        "NO"
    ),
    (
        "1\n4 34 1",
        "NO"
    ),
    (
        "1\n4 35 1",
        "NO"
    ),
    (
        "1\n4 36 1",
        "NO"
    ),
    (
        "1\n4 37 1",
        "NO"
    ),
    (
        "1\n4 38 1",
        "NO"
    ),
    (
        "1\n4 39 1",
        "NO"
    ),
    (
        "1\n4 40 1",
        "NO"
    ),
    (
        "1\n4 41 1",
        "NO"
    ),
    (
        "1\n4 42 1",
        "NO"
    ),
    (
        "1\n4 43 1",
        "NO"
    ),
    (
        "1\n4 44 1",
        "NO"
    ),
    (
        "1\n4 45 1",
        "NO"
    ),
    (
        "1\n4 46 1",
        "NO"
    ),
    (
        "1\n4 47 1",
        "NO"
    ),
    (
        "1\n4 48 1",
        "NO"
    ),
    (
        "1\n4 49 1",
        "NO"
    ),
    (
        "1\n4 50 1",
        "NO"
    ),
    (
        "1\n4 51 1",
        "NO"
    ),
    (
        "1\n4 52 1",
        "NO"
    ),
    (
        "1\n4 53 1",
        "NO"
    ),
    (
        "1\n4 54 1",
        "NO"
    ),
    (
        "1\n4 55 1",
        "NO"
    ),
    (
        "1\n4 56 1",
        "NO"
    ),
    (
        "1\n4 57 1",
        "NO"
    ),
    (
        "1\n4 58 1",
        "NO"
    ),
    (
        "1\n4 59 1",
        "NO"
    ),
    (
        "1\n4 60 1",
        "NO"
    ),
    (
        "1\n4 61 1",
        "NO"
    ),
    (
        "1\n4 62 1",
        "NO"
    ),
    (
        "1\n4 63 1",
        "NO"
    ),
    (
        "1\n4 64 1",
        "NO"
    ),
    (
        "1\n4 65 1",
        "NO"
    ),
    (
        "1\n4 66 1",
        "NO"
    ),
    (
        "1\n4 67 1",
        "NO"
    ),
    (
        "1\n4 68 1",
        "NO"
    ),
    (
        "1\n4 69 1",
        "NO"
    ),
    (
        "1\n4 70 1",
        "NO"
    ),
    (
        "1\n4 71 1",
        "NO"
    ),
    (
        "1\n4 72 1",
        "NO"
    ),
    (
        "1\n4 73 1",
        "NO"
    ),
    (
        "1\n4 74 1",
        "NO"
    ),
    (
        "1\n4 75 1",
        "NO"
    ),
    (
        "1\n4 76 1",
        "NO"
    ),
    (
        "1\n4 77 1",
        "NO"
    ),
    (
        "1\n4 78 1",
        "NO"
    ),
    (
        "1\n4 79 1",
        "NO"
    ),
    (
        "1\n4 80 1",
        "NO"
    ),
    (
        "1\n4 81 1",
        "NO"
    ),
    (
        "1\n4 82 1",
        "NO"
    ),
    (
        "1\n4 83 1",
        "NO"
    ),
    (
        "1\n4 84 1",
        "NO"
    ),
    (
        "1\n4 85 1",
        "NO"
    ),
    (
        "1\n4 86 1",
        "NO"
    ),
    (
        "1\n4 87 1",
        "NO"
    ),
    (
        "1\n4 88 1",
        "NO"
    ),
    (
        "1\n4 89 1",
        "NO"
    ),
    (
        "1\n4 90 1",
        "NO"
    ),
    (
        "1\n4 91 1",
        "NO"
    ),
    (
        "1\n4 92 1",
        "NO"
    ),
    (
        "1\n4 93 1",
        "NO"
    ),
    (
        "1\n4 94 1",
        "NO"
    ),
    (
        "1\n4 95 1",
        "NO"
    ),
    (
        "1\n4 96 1",
        "NO"
    ),
    (
        "1\n4 97 1",
        "NO"
    ),
    (
        "1\n4 98 1",
        "NO"
    ),
    (
        "1\n4 99 1",
        "NO"
    ),
    (
        "1\n4 100 1",
        "NO"
    ),
]

# Run test cases
for input_data, expected_output in test_cases:
    assert run_program_with_captured_io(input_data) == expected_output

print("All test cases passed!")