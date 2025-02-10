#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000. Each test case consists of three positive integers n, m, and k such that 1 ≤ m, k ≤ n ≤ 50.
def func():
    t = int(input())
    for itest in range(0, t, 1):
        n, m, k = map(int, input().split())
        
        if n <= k or n - math.ceil(n / m) <= k:
            print('NO')
        else:
            print('Yes')
        
    #State: t is a positive integer such that \(1 \leq t \leq 1000\), itest is equal to \(t-1\), n, m, and k are the last set of integers inputted during the loop's final iteration. The value of `n` is the `n` from the last input, `m` is the `m` from the last input, and `k` is the `k` from the last input. Depending on the values of `n`, `m`, and `k`, either "YES" or "NO" will have been printed for each iteration, but the variables `n`, `m`, and `k` themselves will retain their last input values.
#Overall this is what the function does:The function processes up to 1000 test cases, each consisting of three positive integers \(n\), \(m\), and \(k\) where \(1 \leq m, k \leq n \leq 50\). For each test case, it checks if \(n \leq k\) or \(n - \lceil \frac{n}{m} \rceil \leq k\). If either condition is true, it prints "NO"; otherwise, it prints "YES". After processing all test cases, the function does not return any value but prints "YES" or "NO" for each test case based on the conditions evaluated.

