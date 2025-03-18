# Import the function from the provided program
from program import func_1

# Define test cases based on the problem description
def test_func_1():
    # Test case 1 from the example
    n1 = 11
    a1 = [0, 0, 0, 1, 0, 2, 0, 3, 1, 1, 4]
    result1 = func_1(n1, a1)
    assert len(result1) == n1, f"Length mismatch: {result1}"
    assert result1.count('a') == 5, f"Incorrect count of 'a': {result1}"
    assert result1.count('b') == 2, f"Incorrect count of 'b': {result1}"
    assert result1.count('r') == 2, f"Incorrect count of 'r': {result1}"
    assert result1.count('c') == 1, f"Incorrect count of 'c': {result1}"
    assert result1.count('d') == 1, f"Incorrect count of 'd': {result1}"

    # Test case 2 from the example
    n2 = 10
    a2 = [0, 0, 0, 0, 0, 1, 0, 1, 1, 0]
    result2 = func_1(n2, a2)
    assert len(result2) == n2, f"Length mismatch: {result2}"
    assert result2.count('c') == 3, f"Incorrect count of 'c': {result2}"
    assert result2.count('o') == 1, f"Incorrect count of 'o': {result2}"
    assert result2.count('d') == 1, f"Incorrect count of 'd': {result2}"
    assert result2.count('e') == 1, f"Incorrect count of 'e': {result2}"
    assert result2.count('f') == 1, f"Incorrect count of 'f': {result2}"
    assert result2.count('r') == 1, f"Incorrect count of 'r': {result2}"
    assert result2.count('s') == 1, f"Incorrect count of 's': {result2}"

    # Test case 3 from the example
    n3 = 1
    a3 = [0]
    result3 = func_1(n3, a3)
    assert len(result3) == n3, f"Length mismatch: {result3}"
    assert result3.count('a') == 1, f"Incorrect count of 'a': {result3}"

    # Test case 4 from the example
    n4 = 8
    a4 = [0, 1, 2, 3, 4, 5, 6, 7]
    result4 = func_1(n4, a4)
    assert len(result4) == n4, f"Length mismatch: {result4}"
    assert result4.count('d') == 1, f"Incorrect count of 'd': {result4}"
    assert result4.count('i') == 1, f"Incorrect count of 'i': {result4}"
    assert result4.count('j') == 1, f"Incorrect count of 'j': {result4}"
    assert result4.count('k') == 1, f"Incorrect count of 'k': {result4}"
    assert result4.count('s') == 1, f"Incorrect count of 's': {result4}"
    assert result4.count('t') == 1, f"Incorrect count of 't': {result4}"
    assert result4.count('r') == 1, f"Incorrect count of 'r': {result4}"
    assert result4.count('a') == 1, f"Incorrect count of 'a': {result4}"

    # Test case 5 from the example
    n5 = 8
    a5 = [0, 0, 0, 0, 0, 0, 0, 0]
    result5 = func_1(n5, a5)
    assert len(result5) == n5, f"Length mismatch: {result5}"
    assert result5.count('a') == 8, f"Incorrect count of 'a': {result5}"

    # Additional edge case
    n6 = 2
    a6 = [0, 0]
    result6 = func_1(n6, a6)
    assert len(result6) == n6, f"Length mismatch: {result6}"
    assert result6.count('a') == 2, f"Incorrect count of 'a': {result6}"

    # Additional edge case
    n7 = 3
    a7 = [0, 1, 1]
    result7 = func_1(n7, a7)
    assert len(result7) == n7, f"Length mismatch: {result7}"
    assert result7.count('a') == 2, f"Incorrect count of 'a': {result7}"
    assert result7.count('b') == 1, f"Incorrect count of 'b': {result7}"

    print("All test cases passed!")

# Run the test cases
test_func_1()