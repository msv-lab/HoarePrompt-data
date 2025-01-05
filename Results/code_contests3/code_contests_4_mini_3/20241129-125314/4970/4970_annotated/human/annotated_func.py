#State of the program right berfore the function call: a is a non-negative integer such that 0 <= a <= 15.
def func():
    print([15, 14, 12, 13, 8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7][int(raw_input())])
#Overall this is what the function does:The function accepts no parameters and prompts the user for an integer input, which it uses to index into a predefined list. It prints the corresponding value from the list based on the input. Since the input is taken from `raw_input()`, if a user inputs an integer outside the range of 0-15, it will raise an `IndexError`. The function does not handle this exception or provide any output for invalid inputs.

