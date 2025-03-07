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
        
    #State: Output State: The final value of `ans` will be the maximum divisor of `x` that is less than or equal to `k`. The variable `l` will contain all such divisors, and `ans` will be the maximum value among these divisors.
    #
    #Explanation: After all iterations of the loop, `ans` will hold the maximum divisor of `x` that is less than or equal to `k`. The loop iterates through all odd numbers up to the square root of `x`, checking if they are divisors of `x` and updating `ans` with the maximum divisor found that meets the criteria. The list `l` keeps track of these divisors, ensuring that `ans` is always updated to the maximum value found.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads two integers \( x \) and \( n \). It calculates the maximum divisor of \( x \) that is less than or equal to \( \frac{x}{n} \) (if \( \frac{x}{n} \geq 1 \)), and prints this value. If \( \frac{x}{n} < 1 \), it directly prints 1. The function implicitly accepts three variables \( t \), \( x \), and \( n \) across multiple test cases, where \( t \) is the number of test cases, and for each test case, \( 1 \leq x \leq 10^8 \) and \( 1 \leq n \leq x \).

