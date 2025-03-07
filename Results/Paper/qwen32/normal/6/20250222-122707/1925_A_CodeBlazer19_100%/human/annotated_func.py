#State of the program right berfore the function call: t is an integer such that 1 <= t <= 676, and for each test case, n and k are integers such that 1 <= n <= 26 and 1 <= k <= 26.
def func():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        print('abcdefghijklmnopqrstuvwxyz'[:k] * n)
        
    #State: The loop has executed `t` times, `i` is `t-1`, `n` is the first integer from the last input, `k` is the second integer from the last input.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `n` and `k`, and then prints a string consisting of the first `k` letters of the alphabet, repeated `n` times.

