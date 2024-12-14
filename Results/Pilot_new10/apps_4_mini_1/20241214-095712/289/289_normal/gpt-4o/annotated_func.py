#State of the program right berfore the function call: n is a positive integer such that 2 <= n <= 10^18, representing the number of players participating in the tournament.
def func():
    n = int(input())
    max_games = n.bit_length() - 1
    print(max_games)
#Overall this is what the function does:The function reads a positive integer `n` from the input, calculates the maximum number of games that can be played in a tournament with `n` players using the formula `n.bit_length() - 1`, and prints that value. The function does not accept any parameters and its operation depends entirely on the value of `n`, which must be between 2 and 10^18.

