#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 25.
def func():
    print[0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 15, 4, 0, 0, 0, 0, 0][input() - 10]
#Overall this is what the function does:The function accepts no parameters, prompts the user for input, and retrieves a value from a predefined list based on the input adjusted by -10. The input must be an integer in the range 1 to 25, as it is used to index the list. If the input is outside this range, an IndexError may occur. The function prints the value found at the adjusted index from the list, which contains a fixed set of integers.

