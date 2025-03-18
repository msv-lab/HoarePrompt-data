#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, and for each test case, x and n are positive integers such that 1 ≤ x ≤ 10^8 and 1 ≤ n ≤ x.
def func_1():
    x, n = list(map(int, input().split()))
    ans = 0
    for i in range(1, isqrt(x) + 1):
        if x % i == 0:
            if n <= x // i:
                ans = max(ans, i)
            elif n <= i:
                ans = max(ans, x // i)
        
    #State: After all iterations, `x` is an integer, `i` is equal to `isqrt(x) + 1`, `ans` is the maximum value of `i` or `x // i` for all divisors `i` of `x` such that `n` is less than or equal to `x // i` or `i`.
    print(ans)
    #This is printed: ans (where ans is the maximum value of i or x // i for all divisors i of x such that n is less than or equal to x // i or i)
#Overall this is what the function does:The function processes multiple test cases, each consisting of positive integers \( x \) and \( n \) (where \( 1 \leq x \leq 10^8 \) and \( 1 \leq n \leq x \)). For each test case, it calculates and prints the maximum value between \( i \) and \( x // i \) for all divisors \( i \) of \( x \) such that \( n \) is less than or equal to either \( x // i \) or \( i \).

