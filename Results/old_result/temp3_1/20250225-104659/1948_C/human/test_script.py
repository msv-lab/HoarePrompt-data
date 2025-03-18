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
def test_program():
    # Test case 1: From the example
    input_data = """4
4
>><<
>>><
2
><
><
4
>>><
>><<
6
>><<><
><>>><"""
    expected_output = "YES\nYES\nNO\nYES"
    assert run_program_with_captured_io(input_data) == expected_output

    # Test case 2: Simple case where robot can reach (2, n)
    input_data = """1
4
>>><
>>><"""
    expected_output = "YES"
    assert run_program_with_captured_io(input_data) == expected_output

    # Test case 3: Simple case where robot cannot reach (2, n)
    input_data = """1
4
<<<>
<<><"""
    expected_output = "NO"
    assert run_program_with_captured_io(input_data) == expected_output

    # Test case 4: Robot oscillates between two cells
    input_data = """1
4
><<>
><><"""
    expected_output = "NO"
    assert run_program_with_captured_io(input_data) == expected_output

    # Test case 5: Robot can reach (2, n) with alternating arrows
    input_data = """1
6
><><><
><><><"""
    expected_output = "YES"
    assert run_program_with_captured_io(input_data) == expected_output

    # Test case 6: Robot cannot reach (2, n) with alternating arrows
    input_data = """1
6
><><><
<><><>"""
    expected_output = "NO"
    assert run_program_with_captured_io(input_data) == expected_output

    # Test case 7: Large input size
    input_data = """1
200000
"{}"
"{}" """.format(">" * 100000 + "<" * 100000, ">" * 100000 + "<" * 100000)
    expected_output = "YES"
    assert run_program_with_captured_io(input_data) == expected_output

    # Test case 8: Another large input size
    input_data = """1
200000
"{}"
"{}" """.format("<" * 100000 + ">" * 100000, "<" * 100000 + ">" * 100000)
    expected_output = "NO"
    assert run_program_with_captured_io(input_data) == expected_output

    # Test case 9: Edge case with minimum n
    input_data = """1
4
><<>
><><"""
    expected_output = "NO"
    assert run_program_with_captured_io(input_data) == expected_output

    # Test case 10: Multiple test cases with different results
    input_data = """3
4
>><<
>>><
4
<<<>
<<><
4
><<>
><><"""
    expected_output = "YES\nNO\nNO"
    assert run_program_with_captured_io(input_data) == expected_output

    print("All test cases passed!")

# Run the tests
test_program()