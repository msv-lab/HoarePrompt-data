#State of the program right berfore the function call: a is a non-negative integer such that 0 <= a <= 15.
def func():
    print([15, 14, 12, 13, 8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7][int(raw_input())])
#Overall this is what the function does:The function does not accept any parameters and prints an element from a predefined list based on user input. The input should be a non-negative integer that indicates the index of the list, which ranges from 0 to 15. If the user inputs an integer outside this range, an IndexError will occur as the list only contains 16 elements (indexed from 0 to 15).

