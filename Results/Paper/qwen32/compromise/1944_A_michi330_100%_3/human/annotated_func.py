#State of the program right berfore the function call: Each test case contains two integers n and k where 1 ≤ n ≤ 100 and 0 ≤ k ≤ \frac{n \cdot (n - 1)}{2}. There are t test cases where 1 ≤ t ≤ 10^3.
def func():
    t = int(input())
    for i in range(0, t, 1):
        n, k = map(int, input().split())
        
        if k >= n - 1:
            print(1)
        else:
            print(n)
        
    #State: The value of `t` remains unchanged, and the output consists of `t` lines, each either `1` or `n`, depending on whether `k >= n - 1` for each test case.
#Overall this is what the function does:The function processes `t` test cases, each consisting of two integers `n` and `k`. For each test case, it outputs `1` if `k` is greater than or equal to `n - 1`, otherwise it outputs `n`.

