#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 676. For each test case, n and k are integers such that 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26.
def func():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        print('abcdefghijklmnopqrstuvwxyz'[:k] * n)
        
    #State: After the loop executes all iterations, `t` remains the same, and `n` and `k` will hold the values from the last iteration. However, the primary output is `t` lines of text, each being the first `k` letters of the alphabet repeated `n` times as specified by the input for each iteration.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `n` and `k`, and prints the first `k` letters of the alphabet repeated `n` times.

