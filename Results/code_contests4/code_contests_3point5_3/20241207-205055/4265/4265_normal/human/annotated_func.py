#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 1000.**
def func():
    n, m = map(int, sys.stdin.readline().split())
    print(n * m) / 2
#Overall this is what the function does:The function `func` reads two integers `n` and `m` from the standard input and calculates their product divided by 2. It does not explicitly return any value. However, there is a syntax error in the code where the result of the division operation is attempted to be printed, which would cause a `TypeError` since `print` does not return a value. Additionally, the code snippet lacks proper error handling for input parsing from `sys.stdin`, which could lead to unexpected behavior if the input format is incorrect.

