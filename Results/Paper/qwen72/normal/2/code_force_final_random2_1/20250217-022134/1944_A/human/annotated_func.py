#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^3, representing the number of test cases. Each test case consists of two integers n and k, where 1 ≤ n ≤ 100 and 0 ≤ k ≤ n * (n - 1) / 2, representing the number of islands and the maximum number of bridges that can be destroyed, respectively.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        print(n if n - k <= 1 else 1)
        
    #State: All iterations of the loop have completed. The variable `t` is an integer where 1 ≤ t ≤ 10^3, and for each of the `t` test cases, the values of `n` and `k` were read from the input and the appropriate output was printed based on the condition `n if n - k <= 1 else 1`. The loop has executed exactly `t` times, and no further iterations will occur.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads two integers `n` and `k`, representing the number of islands and the maximum number of bridges that can be destroyed, respectively. It then prints `n` if `n - k` is less than or equal to 1; otherwise, it prints 1. After processing all `t` test cases, the function completes, and no further actions are performed.

