#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each of the t test cases, a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
def func():
    n = int(input())
    for i in range(n):
        a, b = [int(i) for i in input().split()]
        
        if a % 2 != 0 and b % 2 != 0:
            print('NO')
        elif a / 2 == b and b % 2 != 0 or b / 2 == a and a % 2 != 0:
            print('NO')
        else:
            print('YES')
        
    #State: `t` is a positive integer such that 1 ≤ t ≤ 10^4, `a` and `b` are integers read from the input, `n` must be greater than or equal to the number of iterations executed, and `i` is `n - 1`. For each iteration, if both `a` and `b` are odd, the output is 'NO'. If `a / 2 == b` and `b` is odd, or if `b / 2 == a` and `a` is odd, the output is 'NO'. Otherwise, the output is 'YES'. The values of `a` and `b` are updated with new inputs for each iteration, and the final value of `i` is `n - 1`.
#Overall this is what the function does:The function reads an integer `n` from the input, which represents the number of test cases. For each test case, it reads two integers `a` and `b` from the input. It then checks the following conditions for each pair of `a` and `b`: if both `a` and `b` are odd, it prints 'NO'; if `a / 2 == b` and `b` is odd, or if `b / 2 == a` and `a` is odd, it prints 'NO'; otherwise, it prints 'YES'. After processing all `n` test cases, the function completes without returning any value. The final state of the program is that `n` test cases have been processed, and the appropriate 'YES' or 'NO' output has been printed for each test case.

