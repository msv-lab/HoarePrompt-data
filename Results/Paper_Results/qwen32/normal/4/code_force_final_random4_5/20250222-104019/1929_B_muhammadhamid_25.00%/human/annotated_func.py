#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, n and k are integers such that 2 <= n <= 10^8 and 1 <= k <= 4n - 2.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        if k == 1:
            print(1)
            continue
        
        if k <= 2 * n:
            print(math.ceil(k / 2))
        else:
            print(k // 2 + 1)
        
    #State: After all iterations, the loop will have processed `t` test cases, where for each test case, the values of `n` and `k` are read from the input. If `k` is 1, the output for that test case is 1. Otherwise, the output is calculated as `math.ceil(k / 2)` if `k <= 2 * n`, or `k // 2 + 1` if `k > 2 * n`. The variables `n` and `k` are reset for each new test case, and `t` remains unchanged.
#Overall this is what the function does:The function processes `t` test cases, each consisting of two integers `n` and `k`. For each test case, it outputs a calculated value based on the conditions: if `k` is 1, it outputs 1; if `k` is less than or equal to `2 * n`, it outputs the ceiling of `k / 2`; otherwise, it outputs `k // 2 + 1`.

