#State of the program right berfore the function call: a is an integer such that 0 <= a <= 15.**
def func():
    print([15, 14, 12, 13, 8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7][int(raw_input())])
#Overall this is what the function does:The function `func` does not accept any parameters. It prompts the user for input and prints the corresponding element from a predefined list based on the input provided. The function assumes input will be an integer within the range of 0 to 15. If the input is outside this range, the function will encounter an index out of range error. The function does not explicitly return any value.

