#State of the program right berfore the function call: n is an integer such that 2 <= n <= a + b, a is an integer representing the number of pieces of the first cake (1 ≤ a ≤ 100), and b is an integer representing the number of pieces of the second cake (1 ≤ b ≤ 100).
def func():
    n, b, c = [int(x) for x in raw_input().split()]
    x = max(b, c) / float(min(b, c))
    print(int(ceil(min(b, c) / float(n) * x)))
#Overall this is what the function does:The function accepts three integers `n`, `b`, and `c` from user input, where `n` must be at least 2 and at most the sum of `a` and `b`, with `a` and `b` representing the number of pieces of two cakes. It calculates the ratio of the maximum number of pieces of one cake to the minimum of the two cakes, then computes and prints the ceiling of the product of this ratio and the minimum number of pieces divided by `n`. However, it does not return any value or handle cases where `b` or `c` could be zero, which could lead to a division by zero error.

