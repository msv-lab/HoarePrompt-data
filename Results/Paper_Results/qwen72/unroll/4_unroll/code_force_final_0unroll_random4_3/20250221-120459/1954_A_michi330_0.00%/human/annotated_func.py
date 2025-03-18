#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n, m, and k are integers such that 1 <= m, k <= n <= 50.
def func():
    t = int(input())
    for itest in range(0, t, 1):
        n, m, k = map(int, input().split())
        
        if n <= k or n - math.ceil(n / m) < k:
            print('NO')
        else:
            print('Yes')
        
    #State: The loop has executed `t` times, and for each iteration, the values of `n`, `m`, and `k` were read from user input. If `n` is less than or equal to `k` or if `n - math.ceil(n / m)` is less than `k`, the loop printed 'NO'. Otherwise, it printed 'Yes'. The values of `t`, `n`, `m`, and `k` are unchanged after the loop, but the loop has completed all its iterations.
#Overall this is what the function does:The function `func` reads an integer `t` from user input, representing the number of test cases. For each test case, it reads three integers `n`, `m`, and `k` from user input, where 1 <= m, k <= n <= 50. The function then checks if `n` is less than or equal to `k` or if `n - math.ceil(n / m)` is less than `k`. If either condition is true, it prints 'NO' for that test case; otherwise, it prints 'Yes'. After processing all `t` test cases, the function completes and does not return any value. The values of `t`, `n`, `m`, and `k` are unchanged after the function concludes.

