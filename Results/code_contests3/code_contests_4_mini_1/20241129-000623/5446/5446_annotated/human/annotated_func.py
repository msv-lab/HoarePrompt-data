#State of the program right berfore the function call: n is an integer (2 ≤ n ≤ a + b), a is an integer (1 ≤ a ≤ 100), and b is an integer (1 ≤ b ≤ 100).
def func():
    n, b, c = [int(x) for x in raw_input().split()]
    x = max(b, c) / float(min(b, c))
    print(int(ceil(min(b, c) / float(n) * x)))
#Overall this is what the function does:The function reads three integers `n`, `b`, and `c` from user input, calculates the ratio of the maximum of `b` and `c` to the minimum of `b` and `c`, and then computes the result of multiplying the minimum of `b` and `c` by the ratio divided by `n`. It finally prints the ceiling of this result as an integer. The function does not return any value; it only prints the result.

