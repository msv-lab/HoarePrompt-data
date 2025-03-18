#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3, and for each test case, x is an integer such that 1 ≤ x ≤ 10^8 and n is an integer such that 1 ≤ n ≤ x.
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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 10^3, and for each test case, x is an integer such that 1 ≤ x ≤ 10^8 and n is an integer such that 1 ≤ n ≤ x, with the value of `ans` being the maximum value among the divisors of `x` that are less than or equal to `x // n`.
#Overall this is what the function does:The function processes multiple test cases, each involving three integers \( t \), \( x \), and \( n \). For each test case, it calculates the maximum divisor of \( x \) that is less than or equal to \( x // n \). If \( x // n = 1 \), it prints 1. Otherwise, it iterates through possible divisors of \( x \), checks if they are valid based on the condition, and keeps track of the maximum valid divisor. Finally, it prints the maximum valid divisor found for each test case.

