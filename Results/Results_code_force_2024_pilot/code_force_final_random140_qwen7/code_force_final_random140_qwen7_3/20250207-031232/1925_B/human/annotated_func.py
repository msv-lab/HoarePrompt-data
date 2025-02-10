#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, and for each test case, x and n are positive integers such that 1 ≤ x ≤ 10^8 and 1 ≤ n ≤ x.
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
        
    #State: After the loop executes all iterations, `x` will be a non-negative integer, `n` will be an integer, `i` will be `int(x
#Overall this is what the function does:The function processes multiple test cases, each containing a positive integer \( t \) (1 ≤ \( t \) ≤ 10^3), followed by pairs of positive integers \( x \) and \( n \) (1 ≤ \( x \) ≤ 10^8 and 1 ≤ \( n \) ≤ \( x \)). For each pair \( x \) and \( n \), it calculates and prints the maximum value among 1, any divisor \( i \) of \( x \) where \( i \leq x/n \), and any divisor \( x/i \) of \( x \) where \( x/i \leq x/n \).

