#State of the program right berfore the function call: T is an integer such that 1 <= T <= 100, and X is an integer such that 1 <= X <= 100.
def func():
    t, x = map(float, input().split())
    print(t / x)
#Overall this is what the function does:The function accepts no parameters and reads two floating-point numbers from input, `t` and `x`, which are expected to be within the range of 1 to 100. It then prints the result of the division `t / x`. However, it does not handle the case where `x` is zero, which would lead to a division by zero error, nor does it validate that the inputs are within the specified range or of the correct type.

