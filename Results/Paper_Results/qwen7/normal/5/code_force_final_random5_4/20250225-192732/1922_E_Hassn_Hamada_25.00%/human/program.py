import sys
from typing import Any, List
 
# Open input and output files
stdin = sys.stdin
stdout = sys.stdout
 
# sys.stdin = open('_input.txt', 'r')
# sys.stdout = open('_output.txt', 'w')
 
 
def generate_sequence(number: int, sequence: List[int]) -> int:
    """
    Generates a sequence of numbers based on the input number.
 
    Args:
        number (int): The input number to generate sequence for
        sequence (List[int]): The output sequence 
 
    Returns: 
        int: The size of generated sequence
    """
    assert number >= 0
    if number == 0:
        return 0
 
    size = 1
    while (1 << (size + 1)) - 1 <= number:
        size += 1
 
    for i in range(size):
        sequence.append(i)
 
    result = generate_sequence(number - (1 << size) + 1, sequence)
 
    for i in range(size):
        assert -len(sequence) <= -result - i - 1 <= -1
        sequence[-result - i - 1] += result
 
    return size + result
 
 
# Input processing
test_cases = int(input())
 
for _ in range(test_cases):
    n = int(input())
    result = list()
    size = generate_sequence(n - 1, result)
    print(len(result))
    print(" ".join(map(str, result)))