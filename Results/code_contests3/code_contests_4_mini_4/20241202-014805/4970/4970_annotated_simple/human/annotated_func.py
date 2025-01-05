#State of the program right berfore the function call: a is a non-negative integer such that 0 ≤ a ≤ 15.
def func():
    print([15, 14, 12, 13, 8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7][int(raw_input())])
#Overall this is what the function does:The function accepts user input as an index to print an element from a predefined list of integers, but it does not handle out-of-bounds indices, potentially causing an `IndexError` for inputs less than 0 or greater than 15.

