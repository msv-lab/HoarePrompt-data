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
        
    #State: The variables `a` and `b` will hold the values of the last pair of integers input during the loop's execution, and `i` will be equal to `n`. The initial value of `t` and any other variables not affected by the loop will remain unchanged. The program will have printed 'YES', 'NO', or a combination of both based on the conditions evaluated for each pair of integers.
#Overall this is what the function does:The function reads an integer `n` representing the number of test cases. For each test case, it reads two integers `a` and `b`. It then prints 'YES' if the conditions `a % 2 != 0 and b % 2 != 0` and `a / 2 == b or b / 2 == a` are not met, otherwise it prints 'NO'. The function does not return any value; it only prints output based on the input conditions.

