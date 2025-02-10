#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000. Each test case consists of three positive integers n, m, and k such that 1 ≤ m, k ≤ n ≤ 50.
def func():
    t = int(input())
    for itest in range(0, t, 1):
        n, m, k = map(int, input().split())
        
        if n <= k or n - math.ceil(n / m) <= k:
            print('NO')
        else:
            print('Yes')
        
    #State: Output State: `t` is a positive integer between 1 and 1000, `n` is the first integer input, `m` is the second integer input, `k` is the third integer input, `itest` is equal to `t`, meaning the loop has completed all its iterations. For each iteration, if `n` is less than or equal to `k` or `n - math.ceil(n / m)` is less than or equal to `k`, the condition holds true, resulting in 'NO' being printed. Otherwise, 'Yes' is printed. The values of `n`, `m`, and `k` remain unchanged after the loop completes.
#Overall this is what the function does:The function processes up to 1000 test cases, where for each test case, it reads three positive integers \( n \), \( m \), and \( k \) such that \( 1 \leq m, k \leq n \leq 50 \). It then checks if \( n \leq k \) or \( n - \text{math.ceil}(n / m) \leq k \). If either condition is true, it prints 'NO'; otherwise, it prints 'Yes'. After processing all test cases, the function does not return any value.

