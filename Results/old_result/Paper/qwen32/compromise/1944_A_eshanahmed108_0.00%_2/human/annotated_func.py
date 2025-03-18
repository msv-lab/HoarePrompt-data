#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3, and for each of the t test cases, n and k are integers such that 1 ≤ n ≤ 100 and 0 ≤ k ≤ n * (n - 1) / 2.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        print(n if n - k <= 1 else 1)
        
    #State: For each of the t test cases, the output will be n if n - k is less than or equal to 1; otherwise, the output will be 1. The values of t, n, and k will remain as per the input for each test case.
#Overall this is what the function does:The function processes `t` test cases, each consisting of two integers `n` and `k`. For each test case, it outputs `n` if `n - k` is less than or equal to 1; otherwise, it outputs 1.

