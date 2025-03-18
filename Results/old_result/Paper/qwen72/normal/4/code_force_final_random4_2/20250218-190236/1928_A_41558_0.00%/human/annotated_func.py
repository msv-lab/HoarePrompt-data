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
        
    #State: `t` is an integer such that 1 <= t <= 10^4, `a` and `b` are integers provided by the user input, `n` is equal to the initial value of `n`, and `i` is equal to `n`.
#Overall this is what the function does:The function `func` reads an integer `n` from the user input, representing the number of test cases. For each test case, it reads two integers `a` and `b` from the user input. The function then checks the relationship between `a` and `b` and prints 'NO' if both `a` and `b` are odd, or if one is exactly half of the other. Otherwise, it prints 'YES'. After processing all test cases, the function completes, and the state of the program is such that `n` is equal to the initial value of `n`, and `i` is equal to `n`. The function does not return any value.

