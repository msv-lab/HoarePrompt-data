#State of the program right berfore the function call: a is a non-negative integer such that 0 ≤ a ≤ 15.
def func():
    print([15, 14, 12, 13, 8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7][int(raw_input())])
#Overall this is what the function does:The function accepts a non-negative integer input `a` (expected to be between 0 and 15 inclusive) and prints the value from a predefined list at the index specified by `a`. However, if `a` is outside the range of 0 to 15, it may raise an `IndexError` since the list has only 16 elements (indices 0 to 15). The function does not return a value.

