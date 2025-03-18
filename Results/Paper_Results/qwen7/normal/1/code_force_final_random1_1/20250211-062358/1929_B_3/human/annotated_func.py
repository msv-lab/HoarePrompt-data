#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000, and for each test case, n and k are integers such that 2 <= n <= 10^8 and 1 <= k <= 4n - 2.
def func():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        if 4 * n - 2 == k:
            print(k // 2 + 1)
        else:
            print(ceil(k / 2))
        
    #State: After all iterations of the loop have finished, `t` will be 0, and `n` and `k` will be the values provided in the last iteration of the loop. No further changes will be made to `n` and `k` if `4 * n - 2` does not equal `k`.
#Overall this is what the function does:The function processes a series of test cases defined by the variable `t`. For each test case, it reads two integers `n` and `k`, then checks if `4 * n - 2` equals `k`. If true, it prints `k // 2 + 1`; otherwise, it prints `ceil(k / 2)`. After processing all test cases, the function sets `t` to 0 and retains the values of `n` and `k` from the last test case, without further modification.

