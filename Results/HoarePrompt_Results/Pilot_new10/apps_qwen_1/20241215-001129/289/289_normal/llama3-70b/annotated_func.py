#State of the program right berfore the function call: n is a positive integer such that 2 <= n <= 10^18.
def func():
    n = int(input())
    print(n.bit_length() - 1)
#Overall this is what the function does:The function reads a positive integer `n` from the user, calculates the bit length of `n` minus one, and prints the result.

