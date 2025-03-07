#State of the program right berfore the function call: The function `func` is expected to take two parameters, `n` and `k`, where `n` is an integer representing the number of islands (1 ≤ n ≤ 100), and `k` is an integer representing the maximum number of bridges that can be destroyed (0 ≤ k ≤ n(n - 1)/2). Additionally, the function should be called within a loop that processes multiple test cases, where the number of test cases `t` is an integer (1 ≤ t ≤ 10^3).
def func():
    t = int(input())
    for i in range(0, t, 1):
        n, k = map(int, input().split())
        
        if k >= n - 1:
            print(1)
        else:
            print(n - 1)
        
    #State: The loop has processed `t` test cases, and for each test case, it has printed either `1` if `k` is greater than or equal to `n - 1`, or `n - 1` otherwise. The variables `n` and `k` are updated for each test case based on the input provided, and `i` iterates from 0 to `t-1`. The final value of `i` will be `t-1`.
#Overall this is what the function does:The function `func` processes multiple test cases, where each test case involves two integers `n` and `k`. For each test case, it prints `1` if `k` is greater than or equal to `n - 1`, otherwise it prints `n - 1`. The function does not return any value; it only prints the results to the standard output. After processing all `t` test cases, the function concludes, and the final state of the program is that `t` results have been printed, one for each test case.

