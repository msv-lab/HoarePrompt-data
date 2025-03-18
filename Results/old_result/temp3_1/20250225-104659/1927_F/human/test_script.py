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
    # Test case 1
    input_data = """5
6 6
1 2 1
2 3 1
3 1 1
4 5 1
5 6 1
6 4 1
6 6
1 2 10
2 3 8
3 1 5
4 5 100
5 6 40
6 4 3
6 15
1 2 4
5 2 8
6 1 7
6 3 10
6 5 1
3 2 8
4 3 4
5 3 6
2 6 6
5 4 5
4 1 3
6 4 5
4 2 1
3 1 7
1 5 5
4 6
2 3 2
1 3 10
1 4 1
3 4 7
2 4 5
1 2 2
4 5
2 1 10
3 1 3
4 2 6
1 4 7
2 3 3"""
    expected_output = """1 3
1 2 3
3 3
6 4 5
1 5
4 2 1 6 3
1 4
1 4 3 2
3 3
2 3 1"""
    assert run_program_with_captured_io(input_data) == expected_output

    # Test case 2: Single cycle with minimum edge weight
    input_data = """1
4 4
1 2 1
2 3 2
3 4 3
4 1 4"""
    expected_output = """1 4
1 2 3 4"""
    assert run_program_with_captured_io(input_data) == expected_output

    # Test case 3: Multiple cycles, different minimum edge weights
    input_data = """2
4 5
1 2 5
2 3 1
3 4 2
4 1 3
1 3 4
5 6
1 2 10
2 3 8
3 1 5
4 5 100
5 6 40
6 4 3"""
    expected_output = """1 3
3 1 2
3 3
6 4 5"""
    assert run_program_with_captured_io(input_data) == expected_output

    # Test case 4: Cycle with multiple edges having the same minimum weight
    input_data = """1
5 7
1 2 1
2 3 1
3 4 1
4 5 1
5 1 1
1 3 2
2 4 2"""
    expected_output = """1 5
1 2 3 4 5"""
    assert run_program_with_captured_io(input_data) == expected_output

    # Test case 5: Large graph with many cycles
    input_data = """1
10 15
1 2 1
2 3 2
3 4 3
4 5 4
5 6 5
6 7 6
7 8 7
8 9 8
9 10 9
10 1 10
1 3 11
2 4 12
3 5 13
4 6 14
5 7 15"""
    expected_output = """1 10
1 2 3 4 5 6 7 8 9 10"""
    assert run_program_with_captured_io(input_data) == expected_output

    print("All test cases passed!")

# Run the tests
test_program()