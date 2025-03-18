#State of the program right berfore the function call: Each test case contains two integers n and k where 1 ≤ n ≤ 100 and 0 ≤ k ≤ n * (n - 1) / 2. The input consists of multiple test cases, the number of which is given by the first integer t (1 ≤ t ≤ 10^3).
def func():
    t = int(input())
    for i in range(0, t, 1):
        n, k = map(int, input().split())
        
        if k >= n - 1:
            print(1)
        else:
            print(n - 1)
        
    #State: t is an input integer representing the number of test cases, where 1 ≤ t ≤ 10^3; i is t - 1; n is the first integer from the last input; k is the second integer from the last input. If k is greater than or equal to n - 1, then 1 is printed. Otherwise, n - 1 is printed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers `n` and `k`. For each test case, it prints `1` if `k` is greater than or equal to `n - 1`; otherwise, it prints `n - 1`.

