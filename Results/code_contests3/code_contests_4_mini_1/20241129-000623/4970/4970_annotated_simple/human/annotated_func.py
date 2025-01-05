#State of the program right berfore the function call: a is a non-negative integer such that 0 <= a <= 15.
def func():
    print([15, 14, 12, 13, 8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7][int(raw_input())])
#Overall this is what the function does:The function does not accept any parameters and prints an element from a predefined list based on the user’s input. The input should be a non-negative integer between 0 and 15, which is used as an index to access the list. If the input is out of this range, an IndexError will occur. The function does not return any value.

