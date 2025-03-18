#State of the program right berfore the function call: The function `func` should take two parameters, `n` and `k`, where `n` and `k` are positive integers such that 1 <= n <= 26 and 1 <= k <= 26.
def func():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        print('abcdefghijklmnopqrstuvwxyz'[:k] * n)
        
    #State: `t` iterations have completed, `i` is `t-1`, `n` and `k` are input integers.
#Overall this is what the function does:The function `func` reads an integer `t` from the user, indicating the number of test cases. For each test case, it reads two integers `n` and `k` from the user, where `1 <= n <= 26` and `1 <= k <= 26`. It then prints a string consisting of the first `k` letters of the English alphabet repeated `n` times. After completing all `t` iterations, the function ends, and the state is that `t` iterations have been performed, with the final values of `n` and `k` being the inputs from the last test case.

