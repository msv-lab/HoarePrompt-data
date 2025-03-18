#State of the program right berfore the function call: The function `func` is expected to handle multiple test cases. Each test case consists of three integers n, m, and k where 1 ≤ m, k ≤ n ≤ 50. The function should be able to read input from stdin where the first line contains an integer t (1 ≤ t ≤ 1000) representing the number of test cases, followed by t lines, each containing the integers n, m, and k.
def func():
    t = int(input())
    for itest in range(0, t, 1):
        n, m, k = map(int, input().split())
        
        if n <= k or n - math.ceil(n / m) < k:
            print('NO')
        else:
            print('Yes')
        
    #State: The loop has executed all iterations, and for each test case, the output will be either 'NO' or 'Yes' based on the conditions `n <= k` or `n - math.ceil(n / m) < k`. The variables `t`, `n`, `m`, and `k` will retain their final values from the last iteration, and the loop index `itest` will be equal to `t`.
#Overall this is what the function does:The function `func` reads multiple test cases from standard input. Each test case consists of three integers `n`, `m`, and `k` where 1 ≤ m, k ≤ n ≤ 50. For each test case, the function evaluates whether `n` is greater than `k` and whether `n - math.ceil(n / m)` is not less than `k`. If both conditions are met, it prints 'Yes'; otherwise, it prints 'NO'. After processing all test cases, the function completes, and the variables `t`, `n`, `m`, `k`, and `itest` will retain their final values from the last iteration.

