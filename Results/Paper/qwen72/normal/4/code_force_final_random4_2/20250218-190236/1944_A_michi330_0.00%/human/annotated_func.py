#State of the program right berfore the function call: The function should take two parameters, `n` and `k`, where `n` is an integer representing the number of islands (1 ≤ n ≤ 100) and `k` is an integer representing the maximum number of bridges that can be destroyed (0 ≤ k ≤ n(n-1)/2). The function should be called multiple times for different test cases, and the number of test cases `t` should be an integer (1 ≤ t ≤ 10^3).
def func():
    t = int(input())
    for i in range(0, t, 1):
        n, k = map(int, input().split())
        
        if k >= n - 1:
            print(1)
        else:
            print(n - 1)
        
    #State: `i` is `t`, `t` is the initial value of `t`, and `n` and `k` are the last integers provided by the user. If `k` is greater than or equal to `n - 1`, the function retains the values of `n` and `k` as they were initially. If `k` is less than `n - 1`, the function also retains the values of `n` and `k` as they were initially.
#Overall this is what the function does:The function reads an integer `t` from the user, which represents the number of test cases. For each test case, it reads two integers `n` and `k` from the user, where `n` is the number of islands (1 ≤ n ≤ 100) and `k` is the maximum number of bridges that can be destroyed (0 ≤ k ≤ n(n-1)/2). After processing each test case, the function prints either `1` if `k` is greater than or equal to `n - 1`, or `n - 1` otherwise. The final state of the program after the function concludes is that all test cases have been processed, and the corresponding output has been printed for each test case. The variables `n`, `k`, and `i` retain their last values from the final iteration, and `t` remains unchanged.

