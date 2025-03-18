#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, a and b are integers such that 1 ≤ a, b ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        if a % 2 == 0 or b % 2 == 0:
            print('Yes')
        else:
            print('No')
        
    #State: t is 0, a and b are the last values provided as input, and the program has printed 'Yes' or 'No' for each of the t iterations based on whether at least one of a or b is even.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `a` and `b` and prints 'Yes' if at least one of `a` or `b` is even, otherwise it prints 'No'.

