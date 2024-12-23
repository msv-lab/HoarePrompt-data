#State of the program right berfore the function call: The input is a single integer n, such that n is greater than or equal to 2 and less than or equal to 10^18, representing the number of players to participate in the tournament.
def func():
    n = int(input())
    max_games = n.bit_length() - 1
    print(max_games)
#Overall this is what the function does:The function accepts an integer input from the user, representing the number of players in a tournament, and returns the maximum number of games required to determine the winner, which is calculated as the bit length of the input number minus 1. The function assumes the input is a single integer n, such that n is greater than or equal to 2 and less than or equal to 10^18. After execution, the program prints the calculated maximum number of games to the console, effectively providing the minimum number of rounds needed to complete the tournament, given the number of participants. The function does not handle cases where the input is not an integer or is outside the specified range, which could lead to potential errors or unexpected behavior.

