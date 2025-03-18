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
        
    #State: Postcondition: `t` is a positive integer such that 1 ≤ t ≤ 10^3, `x` is a positive integer such that 1 ≤ x ≤ 10^8, `n` is a positive integer such that 1 ≤ n ≤ x, `ans` is the maximum value between `ans` and all `x // i` for each `i` from 1 to the largest integer `i` such that `i * i` is less than or equal to `x`, and `i` is the last integer within this range that satisfies the conditions in the loop body.
    print(ans)
    #This is printed: the maximum value of x // i for all valid i where i * i <= x
#Overall this is what the function does:For each test case, the function reads three values: \( t \) (a positive integer between 1 and 10^3), \( x \) (a positive integer between 1 and 10^8), and \( n \) (a positive integer between 1 and \( x \)). It then calculates and prints the maximum value of \( x \div i \) for all integers \( i \) from 1 up to the largest integer whose square is less than or equal to \( x \), where \( i \) satisfies the condition \( n \leq x \div i \) or \( n \leq i \).

