#State of the program right berfore the function call: The function `func_1()` will be called with no arguments, but it is expected to handle multiple test cases. Each test case consists of two positive integers `n` and `k` such that 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26.
def func_1():
    n, k = map(int, input().split())
    s = 'abcdefghijklmnopqrstuvwxyz'
    return s[:k] * n
    #The program returns a string consisting of the first `k` characters of the alphabet repeated `n` times.
#Overall this is what the function does:The function `func_1` reads two integers `n` and `k` from the input, where `1 ≤ n ≤ 26` and `1 ≤ k ≤ 26`. It returns a string consisting of the first `k` characters of the alphabet repeated `n` times.

