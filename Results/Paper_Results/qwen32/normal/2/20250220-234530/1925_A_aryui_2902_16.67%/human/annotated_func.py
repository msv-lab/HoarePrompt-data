#State of the program right berfore the function call: t is an integer such that 1 <= t <= 676, and for each of the t test cases, n and k are integers such that 1 <= n <= 26 and 1 <= k <= 26.
def func_1():
    n, k = map(int, input().split())
    s = 'abcdefghijklmnopqrstuvw'
    return s[:k] * n
    #The program returns a string consisting of the first `k` characters of `s` repeated `n` times. Given `s` is `'abcdefghijklmnopqrstuvw'`, the output will be the first `k` letters of the alphabet repeated `n` times.
#Overall this is what the function does:The function reads two integers, `n` and `k`, from the input, and returns a string consisting of the first `k` letters of the alphabet repeated `n` times.

