#State of the program right berfore the function call: The function is designed to handle multiple test cases, where each test case consists of two positive integers n and k, with constraints 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26.
def func():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        print('abcdefghijklmnopqrstuvwxyz'[:k] * n)
        
    #State: The loop has executed `t` times, and for each iteration, it has taken two integers `n` and `k` from the input, and printed a string consisting of the first `k` letters of the alphabet repeated `n` times. The values of `n` and `k` are not retained after each iteration, and `t` remains unchanged.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads two integers `n` and `k` from the input, where `1 ≤ n ≤ 26` and `1 ≤ k ≤ 26`. It then prints a string that consists of the first `k` letters of the alphabet, repeated `n` times. After processing all `t` test cases, the function completes without returning any value. The values of `n` and `k` are not retained between iterations, and `t` remains unchanged throughout the function's execution.

