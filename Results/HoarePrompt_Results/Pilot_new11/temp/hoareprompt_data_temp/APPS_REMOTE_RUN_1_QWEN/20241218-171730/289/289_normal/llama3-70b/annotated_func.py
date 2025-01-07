#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^18.
def func():
    n = int(input())
    print(n.bit_length() - 1)
#Overall this is what the function does:The function reads an integer `n` from the user where `2 ≤ n ≤ 10^18`, and then prints the largest power of 2 that is less than or equal to `n`. Specifically, it calculates and outputs the bit length of `n` minus one. This represents the highest exponent `k` such that \(2^k \leq n\). The function does not return a value but modifies the console output. Potential edge cases include the minimum value (2) and the maximum value (\(10^{18}\)). The function does not handle invalid inputs or values outside the specified range.

