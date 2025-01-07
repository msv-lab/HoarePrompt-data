#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^18, representing the number of players participating in the tournament.
def func():
    n = int(input())
    max_games = n.bit_length() - 1
    print(max_games)
#Overall this is what the function does:The function reads an integer `n` (where \(2 \leq n \leq 10^{18}\)) from input, calculates the maximum number of games required in a single-elimination tournament with `n` players, and prints this value.

