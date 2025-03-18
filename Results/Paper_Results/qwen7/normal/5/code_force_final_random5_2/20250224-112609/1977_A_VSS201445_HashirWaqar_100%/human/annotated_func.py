#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and each test case consists of two positive integers n and m such that 1 ≤ n, m ≤ 100.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        if n >= m and (n - m) % 2 == 0:
            print('YES')
        else:
            print('NO')
        
    #State: Output State: The value of `t` remains a positive integer such that 1 ≤ t ≤ 100. After all the iterations of the loop, `t` will still be the same as its initial value because the loop does not modify `t`. For each iteration, the loop reads two integers `n` and `m`, checks if `n` is greater than or equal to `m` and if their difference is even. If both conditions are met, it prints 'YES', otherwise it prints 'NO'. Regardless of the outcome of these checks, the value of `t` remains unchanged.
    #
    #In summary, the final value of `t` is the same as its initial value, and the loop's output ('YES' or 'NO') depends on the values of `n` and `m` provided during each iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two positive integers \( n \) and \( m \) (where \( 1 \leq n, m \leq 100 \)). For each test case, it checks if \( n \) is greater than or equal to \( m \) and if their difference is even. If both conditions are met, it outputs 'YES'; otherwise, it outputs 'NO'. The function does not return any value but prints the results for each test case. The number of test cases \( t \) (where \( 1 \leq t \leq 100 \)) remains unchanged throughout the execution.

