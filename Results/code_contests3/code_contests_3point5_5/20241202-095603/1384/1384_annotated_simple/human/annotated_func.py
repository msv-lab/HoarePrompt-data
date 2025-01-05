#State of the program right berfore the function call: **Precondition**: **T and X are integers such that 1 <= T <= 100 and 1 <= X <= 100.**
def func():
    t, x = map(float, input().split())
    print(t / x)
#Overall this is what the function does:The function `func` reads two floating-point numbers `t` and `x` from the user input, divides `t` by `x`, and prints the result. The function does not accept any parameters and does not return any value. However, it lacks error handling for cases where the input is not valid or where division by zero may occur.

