#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, n, m, and k are integers such that 1 <= m, k <= n <= 50.
def func():
    t = int(input())
    for itest in range(0, t, 1):
        n, m, k = map(int, input().split())
        
        if n <= k or n - math.ceil(n / m) < k:
            print('NO')
        else:
            print('Yes')
        
    #State: The loop has finished executing `t` times, and for each test case, the output is either 'NO' or 'Yes' based on the conditions `n <= k` or `n - math.ceil(n / m) < k`. The values of `t`, `n`, `m`, and `k` remain unchanged as they are input values and are not modified within the loop.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads three integers `n`, `m`, and `k` from the input, where `1 <= m, k <= n <= 50`. The function then checks if either `n <= k` or `n - math.ceil(n / m) < k` holds true. If either condition is met, it prints 'NO' for that test case; otherwise, it prints 'Yes'. After processing all `t` test cases, the function completes its execution. The values of `t`, `n`, `m`, and `k` are not modified during the function's execution.

