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
        
    #State: Output State: The value of `t` remains a positive integer such that \(1 \leq t \leq 10^4\). The variable `n` is the total number of iterations the loop will execute, which means after all iterations, `i` will be equal to `n-1`. Variables `a` and `b` will hold the values of the last pair of integers entered through input during the last iteration of the loop. No further changes are made to `a` and `b` within the loop based on the given conditions. The loop will continue to execute until it has iterated `n` times, with each iteration checking the conditions on the input values `a` and `b` as described.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two positive integers \(a\) and \(b\). For each test case, it checks if \(a\) and \(b\) satisfy certain conditions. If either \(a\) or \(b\) is odd, or if \(a\) is exactly half of \(b\) or vice versa, it prints 'NO'. Otherwise, it prints 'YES'. After processing all test cases, the function does not return any value but prints 'YES' or 'NO' for each test case based on the conditions checked.

