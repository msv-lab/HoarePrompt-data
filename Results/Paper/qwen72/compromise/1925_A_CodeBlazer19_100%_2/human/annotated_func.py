#State of the program right berfore the function call: The function `func` is expected to take two parameters, `n` and `k`, where `n` and `k` are positive integers such that 1 <= n <= 26 and 1 <= k <= 26.
def func():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        print('abcdefghijklmnopqrstuvwxyz'[:k] * n)
        
    #State: The loop has executed `t` times, and for each iteration, it has read a pair of integers `n` and `k` from the input, and printed the first `k` letters of the English alphabet repeated `n` times. The variables `n` and `k` will hold the values of the last pair of integers read from the input. The variable `t` will remain unchanged.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any value. It reads an integer `t` from the input, representing the number of test cases. For each of the `t` test cases, it reads a pair of integers `n` and `k` from the input, where `1 <= n <= 26` and `1 <= k <= 26`. The function then prints a string consisting of the first `k` letters of the English alphabet repeated `n` times for each test case. After the function concludes, the variable `t` remains unchanged, and the variables `n` and `k` will hold the values of the last pair of integers read from the input.

