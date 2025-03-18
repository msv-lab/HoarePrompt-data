#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, and for each test case, x and n are positive integers such that 1 ≤ x ≤ 10^8 and 1 ≤ n ≤ x.
def func_1():
    x, n = list(map(int, input().split()))
    ans = 0
    for i in range(1, isqrt(x) + 1):
        if x % i == 0:
            if n <= x // i:
                ans = max(ans, i)
            if n <= i:
                ans = max(ans, x // i)
        
    #State: Postcondition: `t` is a positive integer such that \(1 \leq t \leq 10^3\), `x` is an input integer such that \(1 \leq x \leq 10^8\), `n` is an input integer such that \(1 \leq n \leq x\), `ans` is the maximum value between `ans` and `x // i` for all divisors `i` of `x` such that `n <= i` or `n <= x // i`, and `i` has been incremented to `isqrt(x) + 1` after the loop completes.
    print(ans)
    #This is printed: ans (where ans is the maximum value between ans and x // i for all divisors i of x such that n <= i or n <= x // i)
#Overall this is what the function does:The function processes multiple test cases, each defined by input integers \(t\), \(x\), and \(n\). For each test case, it calculates the maximum value between \(ans\) and \(x // i\) for all divisors \(i\) of \(x\) such that \(n \leq i\) or \(n \leq x // i\). After processing all test cases, it prints the final value of \(ans\).

