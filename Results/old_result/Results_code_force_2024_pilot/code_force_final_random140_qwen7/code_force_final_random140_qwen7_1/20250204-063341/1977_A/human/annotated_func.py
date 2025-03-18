#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and for each test case, n and m are positive integers such that 1 ≤ n, m ≤ 100.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        if n < m:
            print('NO')
        elif n & 1 and m & 1 or n % 2 == 0 and m % 2 == 0:
            print('YES')
        
    #State: Output State: After all iterations of the loop have finished, the output state will include a series of 'YES' and 'NO' responses based on the conditions provided within the loop body for each pair of integers \(n\) and \(m\) entered. Specifically, for each pair:
    #
    #- If \(n < m\), the output will be 'NO'.
    #- Otherwise, if \(n\) and \(m\) are both odd or both even, the output will be 'YES'. 
    #
    #All other variables outside the loop (such as the initial value of \(t\)) will retain their original values from the initial state, assuming no further inputs or modifications are made outside the loop during its execution.
#Overall this is what the function does:The function processes multiple test cases, each containing two positive integers \(n\) and \(m\). For each pair, it checks if \(n < m\); if true, it outputs 'NO'. Otherwise, if both \(n\) and \(m\) are either both odd or both even, it outputs 'YES'. The function does not return any value but prints the results for each test case.

