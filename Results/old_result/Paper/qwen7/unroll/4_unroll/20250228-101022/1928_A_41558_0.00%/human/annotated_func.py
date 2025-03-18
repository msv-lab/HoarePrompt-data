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
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 10^4, n is an input integer, and for each iteration of the loop, the program prints 'YES', 'NO' based on the conditions provided, with no overall change in the state of t and n after all iterations.
#Overall this is what the function does:The function processes multiple test cases, each containing two positive integers \(a\) and \(b\). For each test case, it checks if \(a\) and \(b\) meet certain conditions: both being odd, or one being exactly twice the other. If either condition is met, it prints 'NO'. Otherwise, it prints 'YES'. After processing all test cases, the function does not modify the initial values of \(t\), \(n\), \(a\), or \(b\), and only outputs 'YES' or 'NO' for each test case.

