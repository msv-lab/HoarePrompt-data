#State of the program right berfore the function call: the function takes no arguments and the input is a single integer n (1 <= n <= 10^9) that represents the number of squares Sofia wants to draw.
def func():
    n = int(input())
    print(2 * (n.bit_length() - 1) + 2)
#Overall this is what the function does:The function accepts no arguments, takes an integer input `n` from the user, calculates and prints the result of the expression `2 * (n.bit_length() - 1) + 2` without handling any potential exceptions or input validation, assuming the input is a valid integer.

