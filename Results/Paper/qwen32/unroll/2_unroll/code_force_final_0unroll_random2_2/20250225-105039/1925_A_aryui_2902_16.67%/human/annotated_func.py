#State of the program right berfore the function call: The function takes no input arguments. However, the input to the function is provided through standard input and consists of multiple test cases. Each test case contains two positive integers n (1 ≤ n ≤ 26) and k (1 ≤ k ≤ 26). The first line of input contains a single integer t (1 ≤ t ≤ 676) denoting the number of test cases.
def func_1():
    n, k = map(int, input().split())
    s = 'abcdefghijklmnopqrstuvw'
    return s[:k] * n
    #The program returns a string that consists of the first `k` characters of 'abcdefghijklmnopqrstuvw' repeated `n` times.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of two positive integers `n` and `k`. For each test case, it returns a string that consists of the first `k` characters of the alphabet 'abcdefghijklmnopqrstuvw' repeated `n` times.

