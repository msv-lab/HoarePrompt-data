#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^18, representing the number of players participating in the tournament.
def func():
    n = int(input())
    print(n.bit_length() - 1)
#Overall this is what the function does:The function accepts no parameters but reads an integer input `n` (where 2 ≤ n ≤ 10^18) representing the number of players. It computes and prints the largest power of 2 less than or equal to `n` by calculating the bit length of `n` and subtracting one, effectively outputting the exponent of the largest power of 2 that fits within `n`. However, it does not return any value.

