#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 10^9.
def func():
    n = int(input())
    print(2 * (n.bit_length() - 1) + 2)
#Overall this is what the function does:The function accepts no parameters, prompts the user for a positive integer input `n` (where 1 <= n <= 10^9), calculates the bit length of `n`, and prints the result of the expression `2 * (n.bit_length() - 1) + 2`. This effectively calculates twice the number of bits required to represent `n` in binary, minus one, plus two, giving an output that is dependent on the input provided by the user.

