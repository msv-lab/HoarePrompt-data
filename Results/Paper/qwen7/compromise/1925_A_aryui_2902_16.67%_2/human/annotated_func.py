#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 676, and for each test case, n and k are integers such that 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26.
def func_1():
    n, k = map(int, input().split())
    s = 'abcdefghijklmnopqrstuvw'
    return s[:k] * n
    #The program returns a string consisting of the first k characters of 's' repeated n times
#Overall this is what the function does:The function processes the values of `n` and `k` obtained from input, along with a predefined string `s`. It constructs and returns a new string consisting of the first `k` characters of `s`, repeated `n` times.

