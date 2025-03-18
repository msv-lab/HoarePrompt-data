#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each of the t test cases, there are two integers a and b such that 1 <= a, b <= 10^9.
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
        
    #State: A series of 'YES' or 'NO' printed for each of the n test cases based on the conditions specified in the loop.
#Overall this is what the function does:The function reads an integer `n` representing the number of test cases. For each test case, it reads two integers `a` and `b`. It then prints 'NO' if both `a` and `b` are odd or if one is exactly half of the other; otherwise, it prints 'YES'.

