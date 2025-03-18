#State of the program right berfore the function call: t is an integer such that 1 \leq t \leq 1000, and for each test case, a and b are integers such that 1 \le a, b \le 10^9.
def func():
    T = int(input())
    for i in range(T):
        a, b = map(int, input().split())
        
        if a == b:
            print('Bob')
        elif a == 1:
            print('Alice')
        elif b == 1:
            print('Bob')
        elif a % 2 == 1:
            print('Bob')
        elif a % 2 == 0 and b % 2 == 1:
            print('Alice')
        elif a > b:
            print('Bob')
        else:
            print('Alice')
        
    #State: The values of `t` and `T` remain unchanged. For each iteration of the loop, the values of `a` and `b` are read from input and the loop prints either 'Alice' or 'Bob' based on the conditions specified in the loop body. After all iterations, the values of `a` and `b` are not retained and are overwritten in each iteration.
#Overall this is what the function does:The function reads an integer `T` (1 ≤ T ≤ 1000) representing the number of test cases. For each test case, it reads two integers `a` and `b` (1 ≤ a, b ≤ 10^9) from the input. Based on the values of `a` and `b`, the function prints either 'Alice' or 'Bob' according to the following rules: if `a` equals `b`, it prints 'Bob'; if `a` equals 1, it prints 'Alice'; if `b` equals 1, it prints 'Bob'; if `a` is odd, it prints 'Bob'; if `a` is even and `b` is odd, it prints 'Alice'; if `a` is greater than `b`, it prints 'Bob'; otherwise, it prints 'Alice'. The values of `a` and `b` are not retained between iterations.

