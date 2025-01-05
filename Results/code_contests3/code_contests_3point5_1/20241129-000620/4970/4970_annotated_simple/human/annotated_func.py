#State of the program right berfore the function call: a is a non-negative integer such that 0 <= a <= 15.**
def func():
    print([15, 14, 12, 13, 8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7][int(raw_input())])
#Overall this is what the function does:The function `func` does not accept any parameters. When called, it prompts the user for input and based on the input value, it prints a specific element from a predefined list. The input value must be an integer between 0 and 15 (inclusive). If the input value is outside this range, the function will result in an `IndexError` due to accessing an out-of-bounds index in the list. The function does not return any values but provides output based on the input provided.

