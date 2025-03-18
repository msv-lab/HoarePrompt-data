#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^18.
def func():
    n = int(input())
    max_games = n.bit_length() - 1
    print(max_games)
#Overall this is what the function does:The function prompts the user to input an integer `n` (where 2 <= n <= 10^18), calculates the maximum number of games that can be represented using `n` as a power of 2, and prints the result. The function does not return any value.

