#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 676, and for each test case, n and k are positive integers such that 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26.
def func_1():
    n, k = map(int, input().split())
    s = 'abcdefghijklmnopqrstuvw'
    return s[:k] * n
    #The program returns a string consisting of the substring of 's' from the start up to the k-th character, repeated n times.
#Overall this is what the function does:The function reads two integers `n` and `k` from input, where `n` represents the number of repetitions and `k` is the length of the substring to be taken from the string `s`. It then returns a new string consisting of the substring of `s` (which is 'abcdefghijklmnopqrstuvw') from the start up to the `k`-th character, repeated `n` times.

