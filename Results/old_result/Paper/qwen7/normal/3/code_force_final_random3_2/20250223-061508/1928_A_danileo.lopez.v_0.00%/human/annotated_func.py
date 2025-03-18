#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        if a % 2 == 0 or b % 2 == 0:
            print('Yes')
        else:
            print('No')
        
    #State: After the loop executes all iterations, `t` is an integer between 1 and \(10^4\), `_` is equal to the total number of iterations (which is `t`), `a` is the last input integer, and `b` is the second last input integer.
#Overall this is what the function does:The function processes multiple test cases, each containing two positive integers \(a\) and \(b\). For each test case, it checks if either \(a\) or \(b\) is even. If at least one of them is even, it prints 'Yes'; otherwise, it prints 'No'. After processing all test cases, the function ends without returning any value.

