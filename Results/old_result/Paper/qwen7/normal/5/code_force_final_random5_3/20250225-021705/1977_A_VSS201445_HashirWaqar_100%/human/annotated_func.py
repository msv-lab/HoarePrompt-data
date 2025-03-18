#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and each test case consists of two positive integers n and m such that 1 ≤ n, m ≤ 100.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        if n >= m and (n - m) % 2 == 0:
            print('YES')
        else:
            print('NO')
        
    #State: t is a positive integer such that 1 ≤ t ≤ 100, and each test case consists of two positive integers n and m such that 1 ≤ n, m ≤ 100. The value of n and m are determined by the inputs provided during the execution of the loop. After all iterations of the loop have finished, the variable t remains unchanged from its initial value. If the condition `n >= m` and `(n - m) % 2 == 0` is met for any test case, 'YES' is printed; otherwise, 'NO' is printed for that test case.
#Overall this is what the function does:The function reads multiple pairs of positive integers \( n \) and \( m \) (where \( 1 \leq n, m \leq 100 \)) from standard input, checks if \( n \geq m \) and if \( (n - m) \) is even, and prints 'YES' if both conditions are met for any pair; otherwise, it prints 'NO' for that pair. The function does not return any value but prints the result for each pair of integers.

