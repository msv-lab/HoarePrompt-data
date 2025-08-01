import io
import sys

# Mock the input and output for testing
def capture_output(func, input_data):
    sys.stdin = io.StringIO(input_data)
    captured_output = io.StringIO()
    sys.stdout = captured_output
    func()
    sys.stdout = sys.__stdout__
    return captured_output.getvalue().strip()

def test_program():
    # Test case 1: Single element array, k=1
    input_data1 = """1
1 1"""
    expected_output1 = "! 1\n"
    assert capture_output(main, input_data1) == expected_output1

    # Test case 2: Array with two elements, k=2
    input_data2 = """1
2 2"""
    expected_output2 = "! -1\n"
    assert capture_output(main, input_data2) == expected_output2

    # Test case 3: Larger array, k=3
    input_data3 = """1
6 3"""
    expected_output3 = "! 6\n"
    assert capture_output(main, input_data3) == expected_output3

    # Test case 4: Multiple test cases
    input_data4 = """3
1 1
2 2
6 3"""
    expected_output4 = "! 1\n! -1\n! 6\n"
    assert capture_output(main, input_data4) == expected_output4

    # Test case 5: Edge case with maximum n and k
    input_data5 = """1
10000 10000"""
    expected_output5 = "! 100000000\n"  # Assuming the maximum possible value for m
    assert capture_output(main, input_data5) == expected_output5

    # Test case 6: Edge case with minimum n and k
    input_data6 = """1
1 1"""
    expected_output6 = "! 1\n"
    assert capture_output(main, input_data6) == expected_output6

    # Test case 7: k=1 with various n
    input_data7 = """3
1 1
2 1
3 1"""
    expected_output7 = "! 1\n! 2\n! 3\n"
    assert capture_output(main, input_data7) == expected_output7

    # Test case 8: Invalid query handling
    input_data8 = """1
1 1"""
    expected_output8 = "! 1\n"
    # Simulate an invalid query by returning -1
    def mock_input():
        yield "1"
        yield "-1"
    sys.stdin = iter(mock_input())
    assert capture_output(main, input_data8) == expected_output8

    print("All tests passed!")

# Run the test function
test_program()