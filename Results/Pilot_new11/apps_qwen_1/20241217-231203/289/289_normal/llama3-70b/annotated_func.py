#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^18, representing the number of players participating in the tournament.
def func():
    n = int(input())
    print(n.bit_length() - 1)
#Overall this is what the function does:The function reads an integer \( n \) (where \( 2 \leq n \leq 10^{18} \)) from the user, representing the number of players participating in the tournament. It then prints the largest power of 2 that is less than or equal to \( n \), which is equivalent to \( n \) bit-shifted right until the result is odd, minus one. This value indicates the maximum number of rounds required in a single-elimination tournament with \( n \) players. The function does not return any value; instead, it outputs the calculated value directly.

