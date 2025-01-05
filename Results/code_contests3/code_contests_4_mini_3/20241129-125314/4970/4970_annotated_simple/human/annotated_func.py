#State of the program right berfore the function call: a is a non-negative integer such that 0 <= a <= 15.
def func():
    print([15, 14, 12, 13, 8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7][int(raw_input())])
#Overall this is what the function does:The function accepts no parameters and prints a value from a fixed list based on user input as an index; however, it does not handle cases where the input is out of range or invalid, leading to potential errors.

