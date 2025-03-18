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
        
    #State: t is an integer such that 1 <= t <= 10^4, and for each of the t test cases, a and b are integers such that 1 <= a, b <= 10^9; n is an input integer. The loop has finished executing, and for each of the n iterations, 'YES' or 'NO' has been printed based on the conditions provided.
#Overall this is what the function does:The function reads an integer `n` representing the number of test cases. For each test case, it reads two integers `a` and `b`. It then prints 'YES' if neither `a` and `b` are both odd, and `a` is not double `b` and `b` is not double `a`. Otherwise, it prints 'NO'.

