#State of the program right berfore the function call: n is an integer such that 2 <= n <= a + b, a is an integer such that 1 <= a <= 100, and b is an integer such that 1 <= b <= 100.
def func():
    n, b, c = [int(x) for x in raw_input().split()]
    x = max(b, c) / float(min(b, c))
    print(int(ceil(min(b, c) / float(n) * x)))
#Overall this is what the function does:The function accepts three integers `n`, `b`, and `c` from user input, where `n` is in the range of 2 to `a + b` (with `a` in the range of 1 to 100 and `b` in the range of 1 to 100). It calculates the ratio of the maximum of `b` and `c` to the minimum of `b` and `c`, multiplies this ratio by the fraction of `min(b, c)` to `n`, and prints the ceiling of the result as an integer. The function does not return any value.

