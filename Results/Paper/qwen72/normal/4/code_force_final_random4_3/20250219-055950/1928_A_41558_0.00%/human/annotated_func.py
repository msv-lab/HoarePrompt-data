#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, a and b are integers such that 1 <= a, b <= 10^9.
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
        
    #State: `t` is an integer such that 1 <= t <= 10^4, `n` is the input integer, `i` is `n-1`, and for each iteration from 0 to `n-1`, `a` and `b` are integers provided by the user input. If both `a` and `b` are odd, the condition holds and 'NO' is printed. If either `a` is exactly twice `b` or `b` is exactly twice `a`, the condition also holds and 'NO' is printed. Otherwise, 'YES' is printed.
#Overall this is what the function does:The function `func` reads an integer `n` from user input, representing the number of test cases. For each test case, it reads two integers `a` and `b` from user input. The function then checks if both `a` and `b` are odd, or if one is exactly twice the other. If either condition is true, it prints 'NO' for that test case. Otherwise, it prints 'YES'. After processing all test cases, the function completes, and the state of the program is such that `n` test cases have been processed, and the appropriate output ('YES' or 'NO') has been printed for each test case.

