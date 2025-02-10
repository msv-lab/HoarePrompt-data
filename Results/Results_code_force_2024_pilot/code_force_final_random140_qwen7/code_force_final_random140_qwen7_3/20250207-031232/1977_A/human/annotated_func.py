#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and for each test case, n and m are positive integers such that 1 ≤ n, m ≤ 100.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        if n < m:
            print('NO')
        elif n & 1 and m & 1 or n % 2 == 0 and m % 2 == 0:
            print('YES')
        
    #State: `t` is a positive integer such that \(1 \leq t \leq 100\), `n` and `m` are positive integers such that \(1 \leq n, m \leq 100\). After all iterations of the loop, if `n` is less than `m` at any point, the loop will print 'NO' and continue with the next iteration. If `n` is greater than or equal to `m` and both `n` and `m` are either both odd or both even, the loop will print 'YES'. The values of `n` and `m` remain unchanged unless they are updated within the loop, which does not happen based on the given conditions.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three positive integers: `t`, `n`, and `m`. For each test case, it checks if `n` is less than `m`; if true, it prints 'NO'. Otherwise, it checks if `n` and `m` are both odd or both even; if true, it prints 'YES'. The function does not return any value but prints 'YES' or 'NO' based on the specified conditions for each test case.

