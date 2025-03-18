#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, n and k are integers for each test case where 2 ≤ n ≤ 10^8 and 1 ≤ k ≤ 4n - 2.
def func():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        if 4 * n - 2 == k:
            print(k // 2 + 1)
        else:
            print(ceil(k / 2))
        
    #State: `t` is 0, `n` and `k` are input integers. For each iteration, if `4 * n - 2 == k`, the relationship `4 * n - 2 == k` held true and the output was `k // 2 + 1`. Otherwise, the relationship `(4 * n - 2) != k` held true and the output was `ceil(k / 2)`.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads two integers `n` and `k`. If `k` equals `4 * n - 2`, it prints `k // 2 + 1`; otherwise, it prints `ceil(k / 2)`. After processing all test cases, the function completes without returning any value.

