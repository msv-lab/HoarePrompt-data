#State of the program right berfore the function call: T is an integer between 1 and 100 (inclusive), and X is an integer between 1 and 100 (inclusive).
def func():
    t, x = map(float, input().split())
    print(t / x)
#Overall this is what the function does:The function reads two integers, T and X, from user input, both expected to be between 1 and 100 (inclusive). It then calculates and prints the result of T divided by X. However, the function does not handle division by zero, which could occur if X is mistakenly input as zero, despite the initial expectations. Therefore, users should ensure that X is not zero to avoid an error during execution.

