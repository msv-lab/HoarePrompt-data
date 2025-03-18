#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 1000) representing the number of test cases. Each test case consists of three integers n, m, and k (1 ≤ m, k ≤ n ≤ 50), where n is the number of parts of the ribbon, m is the number of colors available, and k is the maximum number of parts Bob can repaint.
def func():
    t = int(input())
    for itest in range(0, t, 1):
        n, m, k = map(int, input().split())
        
        if n <= k or n - math.ceil(n / m) < k:
            print('NO')
        else:
            print('Yes')
        
    #State: `t` remains the same, `itest` equals `t`, `n`, `m`, and `k` hold the values from the last test case.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of three integers `n`, `m`, and `k`. It prints 'NO' if `n` is less than or equal to `k` or if the difference between `n` and the ceiling of `n` divided by `m` is less than `k`. Otherwise, it prints 'YES'. After processing all test cases, the function concludes without altering the input values.

