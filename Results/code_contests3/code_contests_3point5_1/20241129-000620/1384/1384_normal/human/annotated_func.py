#State of the program right berfore the function call: T and X are integers such that 1 <= T <= 100 and 1 <= X <= 100.**
def func():
    t, x = map(float, input().split())
    print(t / x)
#Overall this is what the function does:The function `func` reads two float values `t` and `x` from the input and prints the result of `t / x`. The function does not accept any parameters explicitly. However, it implicitly relies on the user input for `t` and `x`, both of which are expected to be float values. There is no explicit return value from the function.

