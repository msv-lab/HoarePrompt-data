#State of the program right berfore the function call: Each test case contains two integers n and k where 1 ≤ n ≤ 100 and 0 ≤ k ≤ n * (n - 1) / 2. The number of test cases t satisfies 1 ≤ t ≤ 10^3.
def func():
    t = int(input())
    for i in range(0, t, 1):
        n, k = map(int, input().split())
        
        if k >= n - 1:
            print(1)
        else:
            print(n - 1)
        
    #State: t is unchanged; n and k hold the values of the last test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers `n` and `k`. For each test case, it prints `1` if `k` is greater than or equal to `n - 1`, otherwise it prints `n - 1`. The function does not modify the input values `n` and `k` but outputs a result for each test case based on the comparison between `k` and `n - 1`.

