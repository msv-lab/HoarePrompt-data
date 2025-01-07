#State of the program right berfore the function call: n is a positive integer such that 2 ≤ n ≤ 10^18.
def func():
    n = int(input())
    max_games = n.bit_length() - 1
    print(max_games)
#Overall this is what the function does:The function accepts a positive integer `n` (with constraints 2 ≤ n ≤ 10^18), calculates the bit length of `n` (which indicates the number of bits required to represent the integer in binary), and prints this value as `max_games`. This function does not return a value but outputs the result directly.

