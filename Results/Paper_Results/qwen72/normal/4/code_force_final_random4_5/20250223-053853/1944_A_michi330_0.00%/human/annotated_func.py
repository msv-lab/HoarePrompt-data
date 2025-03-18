#State of the program right berfore the function call: The function `func()` is incomplete and does not match the problem description. The correct function definition should include parameters `n` and `k`, and the function should handle multiple test cases as described.
def func():
    t = int(input())
    for i in range(0, t, 1):
        n, k = map(int, input().split())
        
        if k >= n - 1:
            print(1)
        else:
            print(n - 1)
        
    #State: The loop has executed `t` times, and for each iteration, it has read a pair of integers `n` and `k` from the input. If `k` is greater than or equal to `n - 1`, it printed `1`. Otherwise, it printed `n - 1`. The values of `t`, `n`, and `k` are not retained after the loop, but the output of the loop depends on the input provided for each test case.
#Overall this is what the function does:The function reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads two integers `n` and `k` from the input. If `k` is greater than or equal to `n - 1`, it prints `1`. Otherwise, it prints `n - 1`. The function does not return any value, and the values of `t`, `n`, and `k` are not retained after the function execution. The final state of the program is that `t` test cases have been processed, and the appropriate output has been printed for each case.

