#State of the program right berfore the function call: T and X are integers such that 1 <= T <= 100 and 1 <= X <= 100.
def func():
    t, x = map(float, input().split())
    print(t / x)
#Overall this is what the function does:The function accepts no parameters, reads two integers T and X from user input, and prints the result of dividing T by X. If X is 0, a division by zero error will occur, which is not handled in the function. The function thus assumes that X will always be a non-zero integer within the specified range.

