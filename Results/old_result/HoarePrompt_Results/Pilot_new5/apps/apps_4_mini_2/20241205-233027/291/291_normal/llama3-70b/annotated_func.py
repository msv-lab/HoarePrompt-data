#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 10^9.
def func():
    n = int(input())
    print(2 * (n.bit_length() - 1) + 2)
#Overall this is what the function does:The function accepts no parameters, prompts the user to input a positive integer `n` (where 1 <= n <= 10^9), and prints the result of the expression `2 * (n.bit_length() - 1) + 2`. The function does not return any value.

