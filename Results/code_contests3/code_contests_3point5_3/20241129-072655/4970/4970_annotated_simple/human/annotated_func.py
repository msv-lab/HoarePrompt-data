#State of the program right berfore the function call: a is a non-negative integer such that 0 <= a <= 15.**
def func():
    print([15, 14, 12, 13, 8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7][int(raw_input())])
#Overall this is what the function does:The function takes user input and returns the element at the corresponding index from a predefined list [15, 14, 12, 13, 8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7]. The index is determined by the integer input provided by the user. The function assumes the input will always be within the range [0, 15]. No error handling is implemented for inputs outside this range.

