#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are positive integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6. It is also guaranteed that the sum of n and the sum of m over all test cases does not exceed 2 ⋅ 10^6.
def func_1():
    n, k = map(int, input().split())
    ans = n
    root = int(math.sqrt(n)) + 1
    for i in range(2, root + 1):
        cnt = i * i
        
        ans += (n + i) // cnt
        
    #State: Output State: `ans` is the sum of its initial value plus the sum of \((n + i) // cnt\) for each \(i\) from 2 to the largest integer \(i\) such that \(i^2 \leq n\).
    #
    #To break it down in natural language:
    #- The variable `ans` starts with the value of `n`.
    #- For each integer `i` starting from 2 up to the largest integer whose square is less than or equal to `n`, we add \((n + i)\) divided by \(i^2\) to `ans`.
    #- The loop continues until \(i^2\) exceeds `n`.
    #
    #This means that after all iterations of the loop, `ans` will be the initial value of `n` plus the sum of \((n + i) // i^2\) for all integers `i` from 2 to the integer part of the square root of `n` plus one.
    print(ans)
    #This is printed: n + sum((n + i) // i^2 for i in range(2, int(n
#Overall this is what the function does:The function processes a series of test cases, each containing two positive integers \(n\) and \(m\). For each test case, it calculates the value of \(ans\) as the initial value of \(n\) plus the sum of \((n + i) // i^2\) for each integer \(i\) from 2 to the largest integer whose square is less than or equal to \(n\). After processing all test cases, it prints the final value of \(ans\) for each test case.

