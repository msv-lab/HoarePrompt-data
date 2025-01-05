#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ a + b, a is an integer representing the number of pieces of the first cake (1 ≤ a ≤ 100), and b is an integer representing the number of pieces of the second cake (1 ≤ b ≤ 100).
def func():
    n, b, c = [int(x) for x in raw_input().split()]
    x = max(b, c) / float(min(b, c))
    print(int(ceil(min(b, c) / float(n) * x)))
#Overall this is what the function does:The function accepts three integer inputs `n`, `b`, and `c` through user input. It calculates a ratio of the maximum of `b` and `c` to the minimum of `b` and `c`. It then computes the product of this ratio and the fraction of the minimum of `b` and `c` over `n`, and prints the ceiling of the resulting value converted to an integer. There is no check to enforce the precondition that `n` must be at least 2, nor that it must be less than or equal to `a + b`, as those parameters are not used within the function.

