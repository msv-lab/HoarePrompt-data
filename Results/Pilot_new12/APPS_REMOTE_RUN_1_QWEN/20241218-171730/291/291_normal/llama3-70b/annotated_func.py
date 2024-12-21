#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^9.
def func():
    n = int(input())
    print(2 * (n.bit_length() - 1) + 2)
#Overall this is what the function does:The function takes an integer `n` as input, where `1 ≤ n ≤ 10^9`. It calculates and prints the value `2 * (n.bit_length() - 1) + 2`. This value represents the length of the binary representation of `n` minus one, doubled, plus two. There are no explicit return statements, so the function does not return any value. The function does not handle any input validation beyond converting the input to an integer, meaning it assumes the input is always within the specified range. If the input is outside the range, the behavior is undefined.

