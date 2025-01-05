#State of the program right berfore the function call: T and X are integers such that 1 <= T <= 100 and 1 <= X <= 100.
def func():
    t, x = map(float, input().split())
    print(t / x)
#Overall this is what the function does:The function accepts two integers `t` and `x` as input values, calculates the result of `t` divided by `x`, and prints the result. It does not return any value. If `x` is 0, this will cause a division by zero error, but the function does not handle this case explicitly. Therefore, an edge case exists where the function may raise an error if `x` is 0.

