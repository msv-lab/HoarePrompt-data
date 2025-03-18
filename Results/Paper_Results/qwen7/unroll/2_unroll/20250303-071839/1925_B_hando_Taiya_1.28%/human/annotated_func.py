#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, and for each test case, x is a positive integer such that 1 ≤ x ≤ 10^8 and n is a positive integer such that 1 ≤ n ≤ x.
def func_1():
    x, n = list(map(int, input().split()))
    ans = 0
    for i in range(1, isqrt(x) + 1):
        if x % i == 0:
            if n <= x // i:
                ans = max(ans, i)
            elif n <= i:
                ans = max(ans, x // i)
        
    #State: Output State: `t` is a positive integer such that 1 ≤ t ≤ 10³, `x` is a positive integer such that 1 ≤ x ≤ 10⁸, `n` is a positive integer such that 1 ≤ n ≤ x, and `ans` is the maximum value between all `i` and `x // i` where `i` is a divisor of `x` and either `n` ≤ `x // i` or `n` ≤ `i`.
    print(ans)
    #This is printed: max(n, x // n)
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers \( t \), \( x \), and \( n \) where \( 1 \leq t \leq 10^3 \), \( 1 \leq x \leq 10^8 \), and \( 1 \leq n \leq x \). For each test case, it calculates and returns the maximum value between \( n \) and \( x // n \).

