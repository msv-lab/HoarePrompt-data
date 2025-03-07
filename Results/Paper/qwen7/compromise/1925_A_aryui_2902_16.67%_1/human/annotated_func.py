#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 676, and for each test case, n and k are integers such that 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26.
def func_1():
    n, k = map(int, input().split())
    s = 'abcdefghijklmnopqrstuvw'
    return s[:k] * n
    #The program returns a string that is the concatenation of the substring of 's' from index 0 to k (inclusive) repeated n times.
#Overall this is what the function does:The function reads two integers `n` and `k` from input, where `n` represents the number of repetitions and `k` is the length of the substring to be taken from the string `s`. It then returns a new string consisting of the substring of `s` from index 0 to `k` (inclusive), repeated `n` times.

