#State of the program right berfore the function call: The function `func_1` should actually be defined with two parameters `n` and `k`, where `n` and `k` are positive integers such that 1 <= n <= 26 and 1 <= k <= 26.
def func_1():
    n, k = map(int, input().split())
    s = 'abcdefghijklmnopqrstuvwxyz'
    return s[:k] * n
    #The program returns a string that is the first k characters of 'abcdefghijklmnopqrstuvwxyz' repeated n times, where 1 <= n <= 26 and 1 <= k <= 26.
#Overall this is what the function does:The function `func_1` reads two positive integers `n` and `k` from user input, where `1 <= n <= 26` and `1 <= k <= 26`. It then returns a string consisting of the first `k` characters of the English alphabet repeated `n` times.

