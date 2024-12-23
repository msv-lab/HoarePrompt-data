#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^9.
def func():
    n = int(input())
    print(2 * (n.bit_length() - 1) + 2)
#Overall this is what the function does:The function reads an integer `n` from the user where `1 ≤ n ≤ 10^9`. It then calculates and prints the value `2 * (n.bit_length() - 1) + 2`. There are no explicit return values, but the primary action is to compute and display the specified mathematical expression based on the input `n`. Potential edge cases include the minimum value `n=1`, which results in an output of `2`, and larger values of `n` up to `10^9`, where the output will scale accordingly. The function does not handle invalid inputs or values outside the specified range.

