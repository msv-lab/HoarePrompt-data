#State of the program right berfore the function call: t is an integer such that 1 <= t <= 676, and for each of the t test cases, n and k are integers such that 1 <= n <= 26 and 1 <= k <= 26.
def func():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        print('abcdefghijklmnopqrstuvwxyz'[:k] * n)
        
    #State: For each of the `t` test cases, the output consists of the first `k` letters of the English alphabet repeated `n` times.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `n` and `k`, and prints the first `k` letters of the English alphabet repeated `n` times.

