#State of the program right berfore the function call: n is an integer greater than or equal to 2.
def func():
    n = int(input())
    max_games = n.bit_length() - 1
    print(max_games)
#Overall this is what the function does:The function prompts the user for an integer input, calculates the number of bits necessary to represent this integer in binary minus one, prints this value, and implicitly returns None; it does not handle non-integer inputs or negative integers explicitly, which could lead to errors or unexpected behavior.

