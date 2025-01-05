#State of the program right berfore the function call: a is a non-negative integer such that 0 <= a <= 15.**
def func():
    print([15, 14, 12, 13, 8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7][int(raw_input())])
#Overall this is what the function does:The function does not accept any parameters. It prompts the user for input, specifically an integer index, and then prints the corresponding element from a predefined list. The element printed is based on the user input index. The function does not return any value explicitly. Therefore, the actual functionality is to print an element from the list based on user input. There is a missing return statement, and the annotations incorrectly state that the function returns a non-negative integer `a` such that 0 <= a <= 15, which is not accurate.

