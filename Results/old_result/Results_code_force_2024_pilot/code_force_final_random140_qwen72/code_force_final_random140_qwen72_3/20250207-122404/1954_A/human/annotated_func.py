#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 1000, and for each test case, n, m, and k are integers where 1 ≤ m, k ≤ n ≤ 50.
def func():
    t = int(input())
    for itest in range(0, t, 1):
        n, m, k = map(int, input().split())
        
        if n <= k or n - math.ceil(n / m) <= k:
            print('NO')
        else:
            print('Yes')
        
    #State: `t` is an input integer where 1 ≤ t ≤ 1000, `itest` is `t`, and for each of the `t` test cases, `n`, `m`, and `k` were integers where 1 ≤ m, k ≤ n ≤ 50. For each test case, if `n` was less than or equal to `k` or `n - math.ceil(n / m)` was less than or equal to `k`, the output was 'NO'. Otherwise, the output was 'Yes'.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases, where `1 ≤ t ≤ 1000`. For each test case, it reads three integers `n`, `m`, and `k` (where `1 ≤ m, k ≤ n ≤ 50`). It then checks if `n` is less than or equal to `k` or if `n - math.ceil(n / m)` is less than or equal to `k`. If either condition is true, it prints 'NO'; otherwise, it prints 'YES'. After processing all test cases, the function completes, and the program state is unchanged except for the output produced.

