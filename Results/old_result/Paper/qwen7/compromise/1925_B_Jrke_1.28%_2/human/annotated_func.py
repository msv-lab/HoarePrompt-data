#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, and for each test case, x is a positive integer such that 1 ≤ x ≤ 10^8 and n is a positive integer such that 1 ≤ n ≤ x.
def func():
    for _ in range(int(input())):
        x, n = map(int, input().split())
        
        k = x // n
        
        if k == 1:
            print(1)
            continue
        
        ans = 1
        
        for i in range(1 + (1 if x % 2 == 0 else 0), int(x ** 0.5) + 1, 2):
            if x % i == 0:
                l = [ans]
                if i <= k:
                    l.append(i)
                if x // i <= k:
                    l.append(x // i)
                ans = max(l)
        
        print(ans)
        
    #State: Output State: After all iterations of the loop, `ans` will hold the maximum value among all divisors of `x` that are less than or equal to the initial value of `k` (which is `x // n`), and possibly their corresponding quotient when divided into `x`. The variable `i` will be the largest odd integer less than or equal to the square root of `x` after all iterations. The list `l` will contain the maximum divisor found (`ans`), and any other divisors of `x` that are less than or equal to `k` and satisfy the condition `x % i == 0`.
    #
    #In simpler terms, after the loop completes, `ans` will be the greatest divisor of `x` that is less than or equal to `x // n`, and `i` will be the largest odd number less than or equal to the square root of `x`. The list `l` will include `ans` and any other relevant divisors of `x` that meet the specified conditions.
#Overall this is what the function does:The function processes multiple test cases, each involving three integers \( t \), \( x \), and \( n \). For each test case, it calculates the maximum divisor of \( x \) that is less than or equal to \( x // n \), and prints this value. If no such divisor exists, it prints 1. Additionally, it finds the largest odd integer less than or equal to the square root of \( x \) and uses it to determine relevant divisors.

