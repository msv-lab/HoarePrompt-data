#State of the program right berfore the function call: T is an integer such that 1 <= T <= 100, and X is an integer such that 1 <= X <= 100.
def func():
    t, x = map(float, input().split())
    print(t / x)
#Overall this is what the function does:The function accepts no parameters and reads two floating-point numbers from input, which are expected to be integers T and X within the range of 1 to 100. It then prints the result of dividing T by X. If X is 0, it would raise a ZeroDivisionError, as there is no handling for this case in the code.

