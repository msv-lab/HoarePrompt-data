#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3, and for each test case, x is an integer such that 1 ≤ x ≤ 10^8 and n is an integer such that 1 ≤ n ≤ x.
def func():
    for _ in range(int(input())):
        x, n = map(int, input().split())
        
        k = x // n
        
        ans = 1
        
        for i in range(1, int(x ** 0.5) + 2):
            if x % i == 0:
                l = [ans]
                if i <= k:
                    l.append(i)
                if x // i <= k:
                    l.append(x // i)
                ans = max(l)
        
        print(ans)
        
    #State: After the loop executes all iterations, `i` is greater than `int(x
#Overall this is what the function does:The function processes multiple test cases, each involving three integers \( t \), \( x \), and \( n \). For each test case, it calculates and prints the maximum value among the following: 1, any divisor of \( x \) that is less than or equal to \( \frac{x}{n} \), and any quotient when \( x \) is divided by a divisor that is less than or equal to \( \sqrt{x} \).

