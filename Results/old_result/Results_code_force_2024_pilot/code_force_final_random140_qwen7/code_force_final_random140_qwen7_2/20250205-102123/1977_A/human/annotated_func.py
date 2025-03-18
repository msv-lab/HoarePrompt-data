#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and each test case consists of two positive integers n and m such that 1 ≤ n, m ≤ 100.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        if n < m:
            print('NO')
        elif n & 1 and m & 1 or n % 2 == 0 and m % 2 == 0:
            print('YES')
        
    #State: After all iterations of the loop, `t` is a positive integer such that 1 ≤ t ≤ 100, and for each iteration, `n` and `m` are either both odd or both even. The values of `n` and `m` do not change regardless of the condition `n < m`.
#Overall this is what the function does:The function processes multiple pairs of positive integers \( n \) and \( m \) (where \( 1 \leq n, m \leq 100 \)) provided through standard input. For each pair, it checks if \( n \) is less than \( m \). If \( n \) is less than \( m \), it prints 'NO'. Otherwise, it checks if both \( n \) and \( m \) are either odd or even. If they are, it prints 'YES'. After processing all pairs, the function does not return any value but prints 'YES' or 'NO' for each pair based on the specified conditions.

