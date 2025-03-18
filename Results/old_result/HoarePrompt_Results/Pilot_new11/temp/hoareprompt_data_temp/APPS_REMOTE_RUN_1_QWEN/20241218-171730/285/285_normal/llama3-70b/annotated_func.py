#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^9.
def func():
    n = int(input())
    for a in range(n // 1234567 + 1):
        for b in range((n - a * 1234567) // 123456 + 1):
            c = (n - a * 1234567 - b * 123456) // 1234
            if a * 1234567 + b * 123456 + c * 1234 == n:
                print('YES')
                exit()
        
    #State of the program after the  for loop has been executed: `n` is a positive integer greater than or equal to `1234567`, `a` is `a_final`, `b` is `b_final`, `c` is `c_final`, and the equation `a_final * 1234567 + b_final * 123456 + c_final * 1234 == n` holds true. If the loop does not execute, the values of `a`, `b`, and `c` remain as their initial values, which would be `a` is `0`, `b` is `0`, and `c` is `\frac{n}{1234}`, unless the equation does not hold.
    print('NO')
#Overall this is what the function does:The function takes an integer \( n \) as input, where \( 1 \leq n \leq 10^9 \). It attempts to find non-negative integers \( a \), \( b \), and \( c \) such that \( a \cdot 1234567 + b \cdot 123456 + c \cdot 1234 = n \). If such integers exist, it prints 'YES' and exits. If no such integers exist, it prints 'NO'. The function does not return any value. Potential edge cases include when \( n \) is exactly \( 1234567 \), \( 123456 \), or \( 1234 \), as these might affect the range of the loops. Additionally, the function does not handle the case where \( n \) is less than \( 1234567 \); in such cases, the loops will not execute, and the function will print 'NO'.

