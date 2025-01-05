#State of the program right berfore the function call: T is an integer such that 1 <= T <= 100, and X is an integer such that 1 <= X <= 100.
def func():
    t, x = map(float, input().split())
    print(t / x)
#Overall this is what the function does:The function accepts two integers `t` and `x` from user input, where both values must be between 1 and 100. It calculates and prints the result of dividing `t` by `x`. However, there is no error handling for division by zero or invalid input, which could lead to runtime errors if `x` is 0 or if the input is not formatted correctly.

