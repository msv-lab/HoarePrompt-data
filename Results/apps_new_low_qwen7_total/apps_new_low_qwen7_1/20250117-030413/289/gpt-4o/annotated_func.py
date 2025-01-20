#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^18.
def func():
    n = int(input())

max_games = n.bit_length() - 1

print(max_games)
#Overall this is what the function does:The function takes an integer \( n \) as input where \( 2 \leq n \leq 10^{18} \), calculates the maximum number of games that can be played based on the bit length of \( n \) minus one, and prints this value. The function does not return a value; instead, it directly outputs the calculated result. There are no edge cases mentioned in the annotation, but the function correctly performs the intended calculation for the given range of \( n \).

