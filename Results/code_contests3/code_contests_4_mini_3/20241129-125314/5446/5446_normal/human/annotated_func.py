#State of the program right berfore the function call: n is an integer such that 2 <= n <= a + b, a is an integer representing the number of pieces of the first cake (1 ≤ a ≤ 100), and b is an integer representing the number of pieces of the second cake (1 ≤ b ≤ 100).
def func():
    n, b, c = [int(x) for x in raw_input().split()]
    x = max(b, c) / float(min(b, c))
    print(int(ceil(min(b, c) / float(n) * x)))
#Overall this is what the function does:The function accepts three integers: `n`, `b`, and `c`, where `n` is an integer such that \(2 \leq n \leq a + b\) and \(1 \leq b, c \leq 100\). It computes the maximum of `b` and `c`, divides it by the minimum of `b` and `c`, and then calculates how many whole pieces of cake (using the minimum of `b` and `c` divided by `n` times the calculated ratio) are needed. The result is printed as an integer, but the function does not return a value. Additionally, the function may not handle cases where `b` or `c` is zero since it assumes both are at least 1.

