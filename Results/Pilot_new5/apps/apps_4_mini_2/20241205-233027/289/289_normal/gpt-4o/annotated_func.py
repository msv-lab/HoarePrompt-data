#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^18, representing the number of players participating in the tournament.
def func():
    n = int(input())
    max_games = n.bit_length() - 1
    print(max_games)
#Overall this is what the function does:The function reads an integer `n` from user input, which represents the number of players in a tournament (with constraints of 2 ≤ n ≤ 10^18). It calculates and prints the maximum number of games that can be played in a tournament format based on `n`, which is determined using the bit length of `n` minus 1. The function does not return any value.

