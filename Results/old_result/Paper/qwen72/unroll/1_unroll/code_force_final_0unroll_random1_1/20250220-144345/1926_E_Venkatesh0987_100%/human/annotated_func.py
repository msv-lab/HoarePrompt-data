#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 · 10^4, and for each test case, n and k are integers such that 1 ≤ k ≤ n ≤ 10^9.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        s = 0
        
        i = 0
        
        d = n
        
        h = n
        
        p = 1
        
        g = 0
        
        if k > (n + 1) // 2:
            while s < k and d > 0:
                s += (d + 1) // 2
                d -= (d + 1) // 2
                i += 1
            while p <= i - 1:
                g += (h + 1) // 2
                h -= (h + 1) // 2
                p += 1
            f = k - g
            y = 2 ** (i - 1) * (2 * f - 1)
            print(y)
        else:
            print(2 * k - 1)
        
    #State: For each test case, the loop prints a value based on the conditions given. If \( k > \frac{(n + 1)}{2} \), the loop calculates and prints a value \( y \) which is \( 2^{(i - 1)} \times (2 \times f - 1) \), where \( i \) is the number of iterations needed to reach or exceed \( k \) by adding the largest possible odd number from \( n \), and \( f \) is the difference between \( k \) and the sum of the largest possible odd numbers up to \( i-1 \). If \( k \leq \frac{(n + 1)}{2} \), the loop directly prints \( 2 \times k - 1 \). The values of \( t \), \( n \), and \( k \) remain unchanged after the loop execution.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by two integers `n` and `k` (where 1 ≤ k ≤ n ≤ 10^9). For each test case, it prints a value based on the following conditions: If \( k \) is greater than \( \frac{(n + 1)}{2} \), it calculates and prints a value \( y \) which is \( 2^{(i - 1)} \times (2 \times f - 1) \), where \( i \) is the number of iterations needed to reach or exceed \( k \) by adding the largest possible odd number from \( n \), and \( f \) is the difference between \( k \) and the sum of the largest possible odd numbers up to \( i-1 \). If \( k \) is less than or equal to \( \frac{(n + 1)}{2} \), it directly prints \( 2 \times k - 1 \). The values of `t`, `n`, and `k` remain unchanged after the function execution.

