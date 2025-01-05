#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 25.
def func():
    print[0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 15, 4, 0, 0, 0, 0, 0][input() - 10]
#Overall this is what the function does:The function accepts no parameters and prints a value from a pre-defined list based on user input, adjusted by subtracting 10. If the input is outside the range of 10 to 25, it will raise an IndexError due to invalid list indexing.

