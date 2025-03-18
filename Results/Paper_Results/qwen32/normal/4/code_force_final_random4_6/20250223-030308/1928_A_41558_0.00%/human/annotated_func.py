#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each of the t test cases, a and b are integers such that 1 <= a, b <= 10^9.
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
        
    #State: The loop has executed `n` times, where `n` is the number of iterations specified. For each of the `n` iterations, integers `a` and `b` were read from the input, and based on the conditions provided, 'YES' or 'NO' was printed. The value of `i` in the loop ranges from 0 to `n-1`. The variables `t` and `n` remain unchanged throughout the execution.
#Overall this is what the function does:The function reads an integer `n` representing the number of test cases. For each test case, it reads two integers `a` and `b`. It then prints 'YES' if neither `a` nor `b` is odd and they are not such that one is exactly half of the other; otherwise, it prints 'NO'.

