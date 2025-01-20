#State of the program right berfore the function call: n is a positive integer such that 2 <= n <= 10^18.
def func():
    n = int(input())

max_games = n.bit_length() - 1

print(max_games)
#Overall this is what the function does:The function takes no explicit input parameters and reads an integer `n` from the user where \(2 \leq n \leq 10^{18}\). It then calculates the maximum number of games that can be played based on the bit length of `n`, subtracting 1 from it. Finally, it prints the result. There are no return values; the output is printed directly to the console. This function does not handle invalid inputs or edge cases beyond the specified range.

