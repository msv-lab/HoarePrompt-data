#State of the program right berfore the function call: The function takes an integer t (1 ≤ t ≤ 1000) representing the number of test cases. For each test case, it takes three integers n, m, and k (1 ≤ m, k ≤ n ≤ 50) representing the number of parts of the ribbon, the number of available colors, and the maximum number of parts Bob can repaint, respectively.
def func():
    t = int(input())
    for itest in range(0, t, 1):
        n, m, k = map(int, input().split())
        
        if n <= k or n - math.ceil(n / m) < k:
            print('NO')
        else:
            print('Yes')
        
    #State: `t` is an integer representing the number of test cases (1 ≤ t ≤ 1000), `itest` is `t-1`, and for each of the `t` iterations, `n`, `m`, and `k` are integers read from the input. Depending on the condition `n <= k or n - math.ceil(n / m) < k`, either "NO" or "Yes" is printed. The values of `t`, `n`, `m`, and `k` remain unchanged from their input values after each iteration.
#Overall this is what the function does:The function processes `t` test cases, each defined by three integers `n`, `m`, and `k`. For each test case, it determines whether it is possible to repaint up to `k` parts of a ribbon consisting of `n` parts using `m` colors, under the condition that not all parts are repainted and the number of parts that cannot be repainted is less than `k`. It prints "YES" if the condition is met, otherwise "NO".

