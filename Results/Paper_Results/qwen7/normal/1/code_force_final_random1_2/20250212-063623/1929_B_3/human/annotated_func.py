#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, n and k are integers such that 2 ≤ n ≤ 10^8 and 1 ≤ k ≤ 4n - 2.
def func():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        if 4 * n - 2 == k:
            print(k // 2 + 1)
        else:
            print(ceil(k / 2))
        
    #State: The loop has executed `t` times. For each iteration, `n` and `k` are integers obtained from the input. If `4 * n - 2` equals `k`, the output is `k // 2 + 1`. Otherwise, the output is `ceil(k / 2)`. The variable `t` is decremented by 1 after each iteration until it reaches 0.
#Overall this is what the function does:The function processes `t` test cases. For each test case, it reads two integers `n` and `k`. If `4 * n - 2` equals `k`, it prints `k // 2 + 1`; otherwise, it prints `ceil(k / 2)`. After processing all test cases, the function concludes.

