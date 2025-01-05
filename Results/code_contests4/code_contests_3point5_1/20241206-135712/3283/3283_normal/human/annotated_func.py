#State of the program right berfore the function call: x is an integer such that -109 <= x <= 109.**
def func():
    n = abs(input())
    d = int(ceil((sqrt(1 + 8 * n) - 1) / 2))
    print[[0, 2, 1, 0], [1, 0, 0, 2]][n % 2][d % 4] + d
#Overall this is what the function does:The function calculates the absolute value of an input `n`, then performs a series of mathematical operations to determine the result based on the value of `n`. The function prints a value based on the result of the mathematical operations involving `n` and some predefined matrices. The overall result is the sum of a specific element from one of the matrices and `d`, where `d` is derived from `n`. The function does not return any value but prints the final result, which is the sum of a matrix element and `d`.

