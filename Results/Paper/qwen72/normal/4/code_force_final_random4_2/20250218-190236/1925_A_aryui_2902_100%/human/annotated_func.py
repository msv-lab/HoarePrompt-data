#State of the program right berfore the function call: The function should take two parameters, n and k, where n is a positive integer (1 ≤ n ≤ 26) and k is a positive integer (1 ≤ k ≤ 26). The function should be defined as `def func_1(n, k):`.
def func_1():
    n, k = map(int, input().split())
    s = 'abcdefghijklmnopqrstuvwxyz'
    return s[:k] * n
    #The program returns a string that is the first `k` characters of the alphabet 'abcdefghijklmnopqrstuvwxyz' repeated `n` times, where `n` is a positive integer (1 ≤ n ≤ 26) and `k` is a positive integer (1 ≤ k ≤ 26).
#Overall this is what the function does:The function `func_1` takes no parameters and reads two integers `n` and `k` from user input, where `n` and `k` are both positive integers between 1 and 26. It returns a string that consists of the first `k` characters of the English alphabet, repeated `n` times. The function does not modify any external variables or state.

