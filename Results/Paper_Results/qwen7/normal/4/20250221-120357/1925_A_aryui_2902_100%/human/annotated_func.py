#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 676, and for each test case, n and k are positive integers satisfying 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26.
def func_1():
    n, k = map(int, input().split())
    s = 'abcdefghijklmnopqrstuvwxyz'
    return s[:k] * n
    #The program returns a string consisting of the first k characters of 's' repeated n times.
#Overall this is what the function does:The function reads two integers `n` and `k` from input, where `n` and `k` are between 1 and 26. It then returns a string consisting of the first `k` characters of the alphabet ('a' to 'z') repeated `n` times.

