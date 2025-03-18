# Include necessary imports if any
import io
import sys
from program import func_1  # Assuming func_1 is defined in program.py

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

# Test cases for the function func_1
def test_func_1():
    assert func_1(12) == 3  # 1 + 2 = 3
    assert func_1(1) == 1   # 1 = 1
    assert func_1(2) == 2   # 2 = 2
    assert func_1(3) == 3   # 3 = 3
    assert func_1(1434) == 12  # 1 + 4 + 3 + 4 = 12
    assert func_1(2024) == 8  # 2 + 0 + 2 + 4 = 8
    assert func_1(200000) == 2  # 2 + 0 + 0 + 0 + 0 + 0 = 2

# Test cases for the script execution
def test_script():
    input_data = "7\n12\n1\n2\n3\n1434\n2024\n200000"
    expected_output = "51\n1\n3\n6\n18\n12\n8\n2"
    assert run_program_with_captured_io(input_data) == expected_output

# Run the tests
test_func_1()
test_script()

print("All tests passed.")