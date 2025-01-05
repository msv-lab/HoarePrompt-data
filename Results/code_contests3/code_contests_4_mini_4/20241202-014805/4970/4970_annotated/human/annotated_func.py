#State of the program right berfore the function call: a is a single integer such that 0 ≤ a ≤ 15.
def func():
    print([15, 14, 12, 13, 8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7][int(raw_input())])
#Overall this is what the function does:The function does not accept any parameters and prints an element from a predefined list based on user input. The input should be an integer between 0 and 15, which corresponds to the index of the list. If the input is outside this range, it will result in an IndexError.

