#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3, and for each test case, x is an integer such that 1 ≤ x ≤ 10^8 and n is an integer such that 1 ≤ n ≤ x.
def func_1():
    x, n = list(map(int, input().split()))
    ans = 0
    for i in range(1, isqrt(x) + 1):
        if x % i == 0:
            if n <= x // i:
                ans = max(ans, i)
            elif n <= i:
                ans = max(ans, x // i)
        
    #State: `ans` is the maximum value among all `i` such that `x % i == 0` and `n` is less than or equal to `x // i` during the loop's iterations.
    print(ans)
    #This is printed: ans (where ans is the maximum value of i such that x % i == 0 and n <= x // i)
#Overall this is what the function does:For each test case, the function reads three integers \( t \), \( x \), and \( n \). It then finds the maximum integer \( i \) such that \( x \% i == 0 \) (i.e., \( i \) is a divisor of \( x \)) and \( n \leq x // i \). Finally, it prints this maximum value.

