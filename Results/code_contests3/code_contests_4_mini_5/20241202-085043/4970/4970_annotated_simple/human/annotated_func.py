#State of the program right berfore the function call: a is a non-negative integer such that 0 ≤ a ≤ 15.
def func():
    print([15, 14, 12, 13, 8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7][int(raw_input())])
#Overall this is what the function does:The function accepts no parameters and prints an element from a predefined list based on user input. The input is expected to be a non-negative integer within the range of 0 to 15, which corresponds to the indices of the list. If the input is outside this range, the function will raise an IndexError as the list only contains 16 elements (indices 0 to 15). The output of the function is the value at the specified index in the list, but since it does not return a value, it effectively has an undefined return type.

