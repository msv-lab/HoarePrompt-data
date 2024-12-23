#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^18, representing the number of players participating in the tournament.
def func():
    n = int(input())
    print(n.bit_length() - 1)
#Overall this is what the function does:The function reads an integer input `n`, which represents the number of players in a tournament with the constraint that 2 ≤ n ≤ 10^18. It then computes and prints the integer value of `n.bit_length() - 1`. This operation effectively calculates the highest power of 2 less than or equal to `n`, minus one. The function does not take any parameters and also does not handle any edge cases, such as invalid input or values of `n` outside the specified range. After execution, the program does not return any value; it only prints the result.

