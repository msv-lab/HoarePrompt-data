#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 50, and for each test case, n is a positive integer such that 1 ≤ n ≤ 50.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        if n % 2:
            print('NO')
        else:
            s = '110' * (n // 2)
            if len(s) < 200:
                print('YES')
                print(s)
            else:
                print('NO')
        
    #State: Output State: t is an input integer between 1 and 50, inclusive, and after the loop executes all iterations, n takes the last value it was assigned within the loop. The variable s is either '110' repeated a number of times such that its length is less than 200, or does not exist if the condition is not met, and the loop prints 'YES' followed by s or 'NO' based on the conditions inside the loop.
#Overall this is what the function does:The function processes a series of test cases, each defined by a positive integer \( t \) and another positive integer \( n \). For each test case, it checks if \( n \) is even. If \( n \) is odd, it prints 'NO'. If \( n \) is even, it constructs a string \( s \) consisting of '110' repeated \( n/2 \) times. If the length of \( s \) is less than 200, it prints 'YES' followed by \( s \); otherwise, it prints 'NO'. After processing all test cases, the function does not return any value.

