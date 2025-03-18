#State of the program right berfore the function call: The function should take two parameters, n and k, where n is an integer such that 1 ≤ n ≤ 26, and k is an integer such that 1 ≤ k ≤ 26.
def func_1():
    n, k = map(int, input().split())
    s = 'abcdefghijklmnopqrstuvw'
    return s[:k] * n
    #The program returns a string that consists of the first `k` characters of 'abcdefghijklmnopqrstuvw' repeated `n` times, where `n` and `k` are integers provided by the user, and 1 ≤ `n` ≤ 26 and 1 ≤ `k` ≤ 26.
#Overall this is what the function does:The function `func_1` accepts no parameters and reads two integers, `n` and `k`, from user input where 1 ≤ `n` ≤ 26 and 1 ≤ `k` ≤ 26. It returns a string that consists of the first `k` characters of the string 'abcdefghijklmnopqrstuvw' repeated `n` times.

