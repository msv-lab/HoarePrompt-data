#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^18, representing the number of players in the tournament.
def func():
    n = int(input())

max_games = n.bit_length() - 1

print(max_games)
#Overall this is what the function does:The function calculates the maximum number of games that can be played in a single-elimination tournament given the number of players \(n\), where \(2 \leq n \leq 10^{18}\). The function reads the value of \(n\) from the user, computes the maximum number of games using the bit length of \(n\) minus one, and prints the result. The function does not accept any parameters and does not return any value. The final state of the program after the function concludes is that it has printed the calculated maximum number of games.

