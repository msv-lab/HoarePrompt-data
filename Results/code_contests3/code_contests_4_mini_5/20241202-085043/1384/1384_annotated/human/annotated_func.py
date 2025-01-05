#State of the program right berfore the function call: T is an integer such that 1 <= T <= 100, and X is an integer such that 1 <= X <= 100.
def func():
    t, x = map(float, input().split())
    print(t / x)
#Overall this is what the function does:The function reads two floating-point numbers, `t` and `x`, from user input, and prints the result of dividing `t` by `x`. However, it does not handle the case where `x` is zero, which would lead to a division by zero error. Additionally, the function does not accept any parameters.

