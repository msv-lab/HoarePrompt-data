#State of the program right berfore the function call: The function should accept two parameters, n and k, where n is a positive integer (1 ≤ n ≤ 26) and k is a positive integer (1 ≤ k ≤ 26).
def func_1():
    n, k = map(int, input().split())
    s = 'abcdefghijklmnopqrstuvwxyz'
    return s[:k] * n
    #The program returns a string that consists of the first `k` characters of the alphabet string 'abcdefghijklmnopqrstuvwxyz' repeated `n` times.
#Overall this is what the function does:The function `func_1` accepts no parameters and reads two integers, `n` and `k`, from user input, where both `n` and `k` are positive integers between 1 and 26. It returns a string that consists of the first `k` characters of the alphabet string 'abcdefghijklmnopqrstuvwxyz' repeated `n` times. The function does not modify any external state or variables.

