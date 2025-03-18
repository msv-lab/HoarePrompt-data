#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
def func():
    for i in range(int(input())):
        a, b = [int(i) for i in input().split()]
        
        if a % 2 == 0 and b % 2 == 0:
            print('yes')
        elif a % 2 == 0 and a / 2 != b or b % 2 == 0 and b / 2 != a:
            print('yes')
        else:
            print('no')
        
    #State: `t` is a positive integer such that \(1 \leq t \leq 10^4\), `i` is 9999 (since the loop runs `t` times), `a` is the first integer from the input, `b` is the second integer from the input, and the loop has executed `t` times.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three positive integers: `t`, `a`, and `b`. For each test case, it checks specific conditions involving `a` and `b`. If the conditions are met, it prints 'yes'; otherwise, it prints 'no'. After processing all test cases, the function does not return any value but prints the result for each test case.

