#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 1000, and for each test case, n, m, and k are integers where 1 ≤ m, k ≤ n ≤ 50.
def func():
    t = int(input())
    for itest in range(0, t, 1):
        n, m, k = map(int, input().split())
        
        if n <= k or n - math.ceil(n / m) <= k:
            print('NO')
        else:
            print('Yes')
        
    #State: `t` is 0, `itest` is `t-1`, and for each iteration, `n`, `m`, and `k` were input integers. For each test case, if `n` was less than or equal to `k` or the result of `n - math.ceil(n / m)` was less than or equal to `k`, "NO" was printed. Otherwise, "Yes" was printed.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads three integers `n`, `m`, and `k`. It then checks if `n` is less than or equal to `k` or if `n - math.ceil(n / m)` is less than or equal to `k`. If either condition is true, it prints "NO"; otherwise, it prints "Yes". After processing all test cases, the function completes, and the state is such that `t` is 0, `itest` is `t-1`, and the inputs for each test case have been processed and the corresponding output has been printed.

