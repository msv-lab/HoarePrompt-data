#State of the program right berfore the function call: The function `func_1` is called without any arguments. The input is read from standard input where the first line contains a single integer t (1 ≤ t ≤ 676) denoting the number of test cases. Each of the next t lines contains two integers n (1 ≤ n ≤ 26) and k (1 ≤ k ≤ 26).
def func_1():
    n, k = map(int, input().split())
    s = 'abcdefghijklmnopqrstuvwxyz'
    return s[:k] * n
    #The program returns a string consisting of the first k letters of the alphabet repeated n times.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of two integers `n` and `k`. For each test case, it returns a string composed of the first `k` letters of the alphabet repeated `n` times.

