#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^18, representing the number of players participating in the tournament.
def func():
    n = int(input())
    print(n.bit_length() - 1)
#Overall this is what the function does:The function does not accept any parameters and reads an integer input `n` from the user. It then calculates and prints the value of `n.bit_length() - 1`, which represents the highest power of 2 less than or equal to `n`. This means that the output is non-negative as `n` is guaranteed to be at least 2.

