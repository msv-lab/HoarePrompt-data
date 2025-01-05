#State of the program right berfore the function call: T is an integer such that 1 <= T <= 100, and X is an integer such that 1 <= X <= 100.
def func():
    t, x = map(float, input().split())
    print(t / x)
#Overall this is what the function does:The function accepts two integers, T and X, which are read from input and are expected to be within the range of 1 to 100. It computes the division of T by X and prints the result. However, if X is 0, a division by zero error will occur, which is not handled in the code.

