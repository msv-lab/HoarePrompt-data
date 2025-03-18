#State of the program right berfore the function call: Each test case consists of two integers n and k, where 1 ≤ n ≤ 100 and 0 ≤ k ≤ n * (n - 1) / 2. The input starts with an integer t (1 ≤ t ≤ 10^3) representing the number of test cases, followed by t lines, each containing a pair of integers n and k as described.
def func():
    t = int(input())
    for i in range(0, t, 1):
        n, k = map(int, input().split())
        
        if k >= n - 1:
            print(1)
        else:
            print(n)
        
    #State: t is an integer representing the number of test cases, where 1 ≤ t ≤ 10^3; i is equal to t, indicating that the loop has completed all iterations; n and k are the first and second integers from the last input, respectively. The loop has printed 1 if k >= n - 1, or n if k < n - 1, for each of the t test cases.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, and for each test case, it reads two integers `n` and `k`. It then prints `1` if `k` is greater than or equal to `n - 1`, otherwise it prints `n`. This process is repeated for all `t` test cases.

