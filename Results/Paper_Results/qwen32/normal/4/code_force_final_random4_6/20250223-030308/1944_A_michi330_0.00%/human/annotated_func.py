#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3. For each test case, n and k are integers such that 1 ≤ n ≤ 100 and 0 ≤ k ≤ (n * (n - 1)) / 2.
def func():
    t = int(input())
    for i in range(0, t, 1):
        n, k = map(int, input().split())
        
        if k >= n - 1:
            print(1)
        else:
            print(n - 1)
        
    #State: The output is a sequence of `t` numbers, where each number is either `1` or `n - 1` based on the condition `k >= n - 1` for each test case.
#Overall this is what the function does:The function processes `t` test cases, each with two integers `n` and `k`. For each test case, it outputs `1` if `k` is greater than or equal to `n - 1`, otherwise it outputs `n - 1`.

