#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
def func():
    n = int(input())
    for i in range(n):
        a, b = [int(i) for i in input().split()]
        
        if a % 2 != 0 and b % 2 != 0:
            print('NO')
        elif a / 2 == b or b / 2 == a:
            print('NO')
        else:
            print('YES')
        
    #State: Output State: The loop has executed all its iterations, meaning `i` is equal to `n-1`. The variable `t` remains a positive integer such that \(1 \leq t \leq 10^4\). The variable `n` is the total number of iterations the loop was set to run, which must be greater than 0. The variables `a` and `b` are the integers entered by the user on the last iteration of the loop. After the final iteration, if `a` and `b` are both odd, the loop prints 'NO' and does not change their values. If `a / 2` equals `b` or `b / 2` equals `a`, the loop also prints 'NO' and does not change their values. In all other cases, the loop prints 'YES'. The value of `t` remains unchanged throughout the loop executions.
#Overall this is what the function does:The function processes multiple test cases, each containing two positive integers \(a\) and \(b\). For each test case, it checks if \(a\) and \(b\) are both odd, or if either \(a/2\) equals \(b\) or \(b/2\) equals \(a\). If any of these conditions are met, it prints 'NO'. Otherwise, it prints 'YES'. The function does not return any value but prints the result for each test case.

