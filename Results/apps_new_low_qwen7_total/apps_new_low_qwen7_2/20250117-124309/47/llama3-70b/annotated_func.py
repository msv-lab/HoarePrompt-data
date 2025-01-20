#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ n, m ≤ 1 000 000.
def func():
    n, m = map(int, input().split())

count = 0
    for x in range(1, n + 1):
        for y in range(1, m + 1):
            if (x + y) % 5 == 0:
                count += 1
        
    #State of the program after the  for loop has been executed: `count` is `floor(n/5) * m + floor(m/5) * n + floor((n mod 5 + m mod 5)/5)`, `x` is `n + 1`, `y` is `m + 1`, and both `n` and `m` remain unchanged.
    print(count)
#Overall this is what the function does:The function reads two positive integers \( n \) and \( m \) from standard input, where \( 1 \leq n, m \leq 1,000,000 \). It then counts the number of pairs \((x, y)\) where \( 1 \leq x \leq n \), \( 1 \leq y \leq m \), and the sum \( x + y \) is divisible by 5. The function prints the count of such pairs. If either \( n \) or \( m \) is less than 5, the count is adjusted accordingly. After execution, the function returns the count of valid pairs, and the original values of \( n \) and \( m \) remain unchanged.

