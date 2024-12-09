#State of the program right berfore the function call: n is a positive integer such that 2 ≤ n ≤ 10^18.
def func():
    n = int(input())
    print(n.bit_length() - 1)
#Overall this is what the function does:The function accepts no parameters, prompts the user for a positive integer input `n` (where 2 ≤ n ≤ 10^18), and prints the number of bits required to represent `n` in binary minus one. This effectively gives the exponent of the highest power of two less than or equal to `n`. It does not handle invalid inputs or edge cases where `n` is outside the specified range, as the function assumes valid input is always provided.

