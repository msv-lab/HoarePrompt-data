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
        
    #State: `t` is a positive integer such that \(1 \leq t \leq 10^4\), `n` is the total number of iterations the loop will execute, `i` is equal to `n-1`, `a` is the first integer entered during the last iteration, and `b` is the second integer entered during the last iteration. If both `a` and `b` are odd, no changes are made. If `a / 2 == b` or `b / 2 == a`, no changes are made. Otherwise, no changes are made.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three positive integers: `t`, `a`, and `b`. For each test case, it checks if `a` and `b` are both odd, or if `a / 2` equals `b` or `b / 2` equals `a`. If either condition is met, it prints 'NO'. Otherwise, it prints 'YES'. After processing all test cases, the function does not return any value but prints 'YES' or 'NO' for each test case based on the conditions specified.

