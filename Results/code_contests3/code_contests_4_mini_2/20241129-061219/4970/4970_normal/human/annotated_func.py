#State of the program right berfore the function call: a is a single integer such that 0 ≤ a ≤ 15.
def func():
    print([15, 14, 12, 13, 8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7][int(raw_input())])
#Overall this is what the function does:The function prompts the user for an integer input, and prints the corresponding value from a predefined list based on that input; it expects the input to be between 0 and 15, and will raise an `IndexError` if the input is outside this range.

