#State of the program right berfore the function call: The input is an integer n, such that n is greater than or equal to 2 and less than or equal to 10^18, representing the number of players participating in the tournament.
def func():
    n = int(input())
    print(n.bit_length() - 1)
#Overall this is what the function does:The function reads an integer from the input, calculates the number of bits required to represent the integer in binary, subtracts 1 from this value, and prints the result. If the input is not a valid integer, it may raise a ValueError.

