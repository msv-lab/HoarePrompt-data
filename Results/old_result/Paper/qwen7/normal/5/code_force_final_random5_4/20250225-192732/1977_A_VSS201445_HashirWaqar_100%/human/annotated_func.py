#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and each test case consists of two positive integers n and m such that 1 ≤ n, m ≤ 100.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        if n >= m and (n - m) % 2 == 0:
            print('YES')
        else:
            print('NO')
        
    #State: Output State: The output state after the loop executes all the iterations is that `n` and `m` retain their original values throughout all iterations. The loop processes each pair of `n` and `m` independently based on the given conditions and prints 'YES' or 'NO' accordingly but does not modify the values of `n` and `m` between iterations. Therefore, regardless of the number of iterations, `n` and `m` will always reflect the values they had at the start of the loop.
#Overall this is what the function does:The function processes a series of pairs of positive integers \( n \) and \( m \) (where \( 1 \leq n, m \leq 100 \)) derived from a positive integer \( t \) (where \( 1 \leq t \leq 100 \)). For each pair, it checks if \( n \geq m \) and if \( n - m \) is even. If both conditions are met, it prints 'YES'; otherwise, it prints 'NO'. The function does not modify the values of \( n \) and \( m \) between iterations and retains their original values throughout the process.

