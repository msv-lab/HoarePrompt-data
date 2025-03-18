#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 50, and for each test case, n is an integer such that 2 ≤ n ≤ 10^3.
def func():
    t = int(input())
    while t:
        t -= 1
        
        n = int(input())
        
        for i in range(1, n + 1):
            print('1', end=' ')
            print(i)
        
        print(' ')
        
    #State: Output State: `t` is 1000, `i` is 3003, `n` is 1000.
    #
    #Explanation: After the loop executes all its iterations, the variable `t` remains unchanged at 1000 because it is decremented by 1 in each iteration but starts at 1000 and reaches 0 after 1000 iterations. The variable `i` starts at 1002 and increments by 1 for each iteration, so after 1000 iterations, `i` will be `1002 + 1000 - 1 = 2001`. However, the provided pattern suggests that `i` is calculated as `1001 + n`, where `n` is the original value. Given that `n` is 1000, `i` will be `1001 + 1000 = 2001`, but the pattern seems to increment by 3 each time, leading to `i` being `1001 + 3 * 3 = 3003` after 3 iterations and then continuing this pattern for all 1000 iterations. Therefore, `i` is 3003 after all iterations. The value of `n` remains 1000 as it was initially set.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads two integers \( t \) and \( n \), where \( 1 \leq t \leq 50 \) and \( 2 \leq n \leq 10^3 \). It then prints \( t \) lines, each containing \( n \) occurrences of the number 1 followed by the line number starting from 1. After processing all test cases, the function does not return any value but outputs the specified pattern.

