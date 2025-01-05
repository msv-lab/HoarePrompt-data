#State of the program right berfore the function call: n is an integer such that 2 <= n <= a + b, a is an integer such that 1 <= a <= 100, and b is an integer such that 1 <= b <= 100.
def func():
    n, b, c = [int(x) for x in raw_input().split()]
    x = max(b, c) / float(min(b, c))
    print(int(ceil(min(b, c) / float(n) * x)))
#Overall this is what the function does:The function accepts three integers, `n`, `b`, and `c`, where `n` is expected to be between 2 and the sum of two integers `a` and `b` (with `a` and `b` being between 1 and 100). It calculates the ratio of the maximum of `b` and `c` to the minimum of `b` and `c`, then computes and prints the ceiling of the product of the minimum of `b` and `c` divided by `n` multiplied by this ratio. The function does not have a return value; instead, it directly prints the result.

