#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. Each of the following t lines contains two integers n and k such that 2 <= n <= 10^8 and 1 <= k <= 4n - 2.
def func():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        if 4 * n - 2 == k:
            print(k // 2 + 1)
        else:
            print(ceil(k / 2))
        
    #State: For each of the `t` lines, the output will be either `k // 2 + 1` if `k == 4 * n - 2`, or `(k + 1) // 2` otherwise.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of two integers `n` and `k`. For each test case, it outputs a calculated value: `k // 2 + 1` if `k` equals `4 * n - 2`, otherwise it outputs `(k + 1) // 2`.

