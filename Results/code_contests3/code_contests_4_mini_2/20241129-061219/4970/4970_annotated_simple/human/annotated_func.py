#State of the program right berfore the function call: a is a non-negative integer such that 0 ≤ a ≤ 15.
def func():
    print([15, 14, 12, 13, 8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7][int(raw_input())])
#Overall this is what the function does:The function prompts the user to input an integer, which it uses to index into a predefined list of integers. It prints the corresponding value from the list based on the input index, but it does not handle cases where the input index is out of range, leading to potential IndexError exceptions.

