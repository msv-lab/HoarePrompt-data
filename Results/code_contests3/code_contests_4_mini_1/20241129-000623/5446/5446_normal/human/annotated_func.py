#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ a + b, a and b are integers representing the number of pieces of two cakes, and both a and b are positive integers such that 1 ≤ a, b ≤ 100.
def func():
    n, b, c = [int(x) for x in raw_input().split()]
    x = max(b, c) / float(min(b, c))
    print(int(ceil(min(b, c) / float(n) * x)))
#Overall this is what the function does:The function reads three integers `n`, `b`, and `c` from input, where `n` is an integer such that 2 ≤ n ≤ a + b, and both `a` and `b` are positive integers between 1 and 100. It calculates the ratio of the maximum of `b` and `c` to the minimum of `b` and `c`, then computes the ceiling of the product of the ratio and the minimum of `b` and `c` divided by `n`, and prints the resulting integer. The function does not handle any errors or edge cases related to the input values.

