#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^18, representing the number of players participating in the tournament.
def func():
    n = int(input())
    max_games = n.bit_length() - 1
    print(max_games)
#Overall this is what the function does:The function reads an integer input `n` from the user, which represents the number of players in a tournament and is assumed to be in the range from 2 to \(10^{18}\). It then calculates the maximum number of games that can be played in a single-elimination tournament format based on the input, determining this by computing the bit length of `n` and subtracting one. Finally, it prints the computed maximum number of games. The function does not return a value; it only outputs the result. Notably, there are no checks for input validity beyond the described constraints, and the function does not handle scenarios where the input might be invalid or non-integer.

