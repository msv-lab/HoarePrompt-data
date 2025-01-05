#State of the program right berfore the function call: T is an integer such that 1 <= T <= 100, and X is an integer such that 1 <= X <= 100.
def func():
    t, x = map(float, input().split())
    print(t / x)
#Overall this is what the function does:The function accepts two integers `t` and `x` as input, where both integers must be between 1 and 100. It calculates the division of `t` by `x` and prints the result. However, it does not return any value or handle potential division errors, such as dividing by zero, which is not possible with the given constraints.

