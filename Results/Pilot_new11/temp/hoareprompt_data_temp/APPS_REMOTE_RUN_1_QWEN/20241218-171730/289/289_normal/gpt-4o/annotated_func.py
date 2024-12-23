#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^18, representing the number of players in the tournament.
def func():
    n = int(input())
    max_games = n.bit_length() - 1
    print(max_games)
#Overall this is what the function does:The function reads an integer `n` from the user, which represents the number of players in a tournament. It then calculates the maximum number of rounds needed in a single-elimination tournament using `n.bit_length() - 1`. Finally, it prints the result. The function accepts no parameters and does not return any value. The postcondition is that after the function execution, the program will have printed the maximum number of rounds required for the tournament. This calculation assumes that each round halves the number of remaining players until one player remains. Potential edge cases include when `n` is 1 (which should print 0 since no games are needed) or when `n` is outside the range 2 to \(10^{18}\), in which case the bit length calculation still applies but the initial precondition check is implied by the bit length calculation itself.

