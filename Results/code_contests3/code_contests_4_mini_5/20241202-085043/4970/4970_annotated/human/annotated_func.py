#State of the program right berfore the function call: a is a single integer such that 0 ≤ a ≤ 15.
def func():
    print([15, 14, 12, 13, 8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7][int(raw_input())])
#Overall this is what the function does:The function accepts no parameters and prints an element from a predefined list based on user input, which must be an integer between 0 and 15. If the input is outside this range, the function may raise an IndexError, as it does not handle invalid inputs or provide any return value.

