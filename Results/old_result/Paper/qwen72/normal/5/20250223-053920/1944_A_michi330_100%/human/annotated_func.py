#State of the program right berfore the function call: The function `func` is expected to take two parameters, `n` and `k`, where `n` is an integer representing the number of islands (1 ≤ n ≤ 100), and `k` is an integer representing the maximum number of bridges that can be destroyed (0 ≤ k ≤ n(n - 1)/2). The function should be called within a loop that processes multiple test cases, where the number of test cases `t` is an integer (1 ≤ t ≤ 10^3).
def func():
    t = int(input())
    for i in range(0, t, 1):
        n, k = map(int, input().split())
        
        if k >= n - 1:
            print(1)
        else:
            print(n)
        
    #State: The loop has finished executing all `t` iterations. For each iteration, if `k` was greater than or equal to `n - 1`, the output was `1`. Otherwise, the output was `n`. The values of `t`, `n`, and `k` are unchanged after the loop, but the loop has processed `t` test cases and printed the corresponding output for each.
#Overall this is what the function does:The function `func` processes a series of test cases. It reads an integer `t` indicating the number of test cases. For each test case, it reads two integers `n` and `k`, where `n` is the number of islands and `k` is the maximum number of bridges that can be destroyed. If `k` is greater than or equal to `n - 1`, the function prints `1`. Otherwise, it prints `n`. After processing all `t` test cases, the function has printed the appropriate output for each case, and the values of `t`, `n`, and `k` are unchanged. The function does not return any value.

