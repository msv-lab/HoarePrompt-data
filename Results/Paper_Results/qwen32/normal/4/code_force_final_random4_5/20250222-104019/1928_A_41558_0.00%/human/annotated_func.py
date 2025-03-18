#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, a and b are integers such that 1 ≤ a, b ≤ 10^9.
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
        
    #State: The loop has executed `n` times, and for each iteration, it reads a pair of integers `a` and `b`. If both `a` and `b` are odd, it prints 'NO'. If one of `a` or `b` is twice the other, it prints 'NO'. Otherwise, it prints 'YES'. The values of `t`, `n`, and the relationship between `a` and `b` for each iteration are as specified in the input.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `a` and `b`. It prints 'NO' if both `a` and `b` are odd or if one is exactly twice the other. Otherwise, it prints 'YES'.

