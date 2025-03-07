#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 2 ≤ n ≤ 500; x is a list of n-1 integers where 1 ≤ x_i ≤ 500, and the sum of all n values across all test cases does not exceed 2 · 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        x = list(map(int, input().split()))
        
        a = [0] * n
        
        a[0] = 1000
        
        for i in range(1, n):
            a[i] = a[i - 1] + x[i - 1]
        
        print(*a)
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an input integer such that 2 ≤ n ≤ 500, `x` is a list of integers read from the input, `a` is a list of length `n` where `a[0]` is 1000 and for each `i` from 1 to `n-1`, `a[i]` is `1000 + sum(x[:i])`, `i` is `n-1`. This state is repeated for each of the `t` test cases.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a list `x` of `n-1` integers. For each test case, it generates a list `a` of length `n` where `a[0]` is always 1000, and each subsequent element `a[i]` (for `i` from 1 to `n-1`) is calculated as `1000 + sum(x[:i])`. The function prints the list `a` for each test case. After processing all test cases, the function completes without returning any value.

