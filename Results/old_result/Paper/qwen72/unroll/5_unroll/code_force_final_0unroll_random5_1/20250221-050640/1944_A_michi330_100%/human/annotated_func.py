#State of the program right berfore the function call: The function `func` is expected to take two parameters, `n` and `k`, where `n` is an integer representing the number of islands (1 ≤ n ≤ 100) and `k` is an integer representing the maximum number of bridges that can be destroyed (0 ≤ k ≤ n(n-1)/2). The function should be called within a loop that processes multiple test cases, where the number of test cases `t` is an integer (1 ≤ t ≤ 10^3).
def func():
    t = int(input())
    for i in range(0, t, 1):
        n, k = map(int, input().split())
        
        if k >= n - 1:
            print(1)
        else:
            print(n)
        
    #State: The loop has finished executing all `t` iterations. For each iteration, if `k` is greater than or equal to `n - 1`, the output is `1`. Otherwise, the output is `n`. The variable `t` is now 0, as the loop has completed all its iterations. The values of `n` and `k` are not retained after each iteration, as they are re-assigned in each iteration based on the input.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by two integers `n` and `k`. For each test case, it prints `1` if `k` is greater than or equal to `n - 1`, otherwise it prints `n`. After processing all test cases, the function completes and the variable `t` (number of test cases) is no longer relevant. The values of `n` and `k` are re-assigned in each iteration and do not persist beyond the loop.

