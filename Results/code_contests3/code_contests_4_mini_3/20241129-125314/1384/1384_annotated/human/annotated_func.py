#State of the program right berfore the function call: T is an integer such that 1 <= T <= 100, and X is an integer such that 1 <= X <= 100.
def func():
    t, x = map(float, input().split())
    print(t / x)
#Overall this is what the function does:The function accepts two integers `t` and `x` (both within the range of 1 to 100) from user input, calculates the division of `t` by `x`, and prints the result. However, the function does not handle potential division by zero errors, which would occur if `x` were 0, even though the input constraints specify that `x` must be at least 1. Additionally, the function does not return any value.

