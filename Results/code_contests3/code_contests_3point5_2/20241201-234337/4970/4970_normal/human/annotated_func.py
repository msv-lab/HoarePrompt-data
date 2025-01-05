#State of the program right berfore the function call: a is an integer such that 0 ≤ a ≤ 15.**
def func():
    print([15, 14, 12, 13, 8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7][int(raw_input())])
#Overall this is what the function does:The function does not accept any parameters. It reads an integer input and prints a value from a predefined list based on the input. The printed value corresponds to the index of the input value in the list [15, 14, 12, 13, 8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7]. However, the code does not handle cases where the input is outside the range of the list indices.

