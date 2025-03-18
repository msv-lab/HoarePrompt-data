#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, a and b are integers such that 1 ≤ a, b ≤ 10^9.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 1000, `T` is equal to the number of iterations the loop executed, and `i` is `T - 1`. For each iteration of the loop, `a` and `b` are integers provided by the user input. If `a` is equal to `b`, then `a` and `b` are the same integers provided by the user input. If `a` is not equal to `b`, then `a` and `b` are different integers provided by the user input. If `a` is 1, it remains 1, and if `b` is 1, `a` is not equal to `b`. If `b` is not 1, then `a` is not equal to `b` and `b` is not equal to 1. If `a` is odd, then `a` is an odd integer. If `a` is even and `b` is odd, then `a` is even and `b` is odd. If `a` > `b`, `a` is greater than `b`. Otherwise, `a` is less than or equal to `b`.
#Overall this is what the function does:The function `func` reads an integer `T` from user input, indicating the number of test cases to process. For each test case, it reads two integers `a` and `b` from user input. It then prints the name 'Bob' or 'Alice' based on the following conditions: if `a` equals `b`, it prints 'Bob'; if `a` is 1, it prints 'Alice'; if `b` is 1, it prints 'Bob'; if `a` is odd, it prints 'Bob'; if `a` is even and `b` is odd, it prints 'Alice'; if `a` is greater than `b`, it prints 'Bob'; otherwise, it prints 'Alice'. After processing all test cases, the function concludes, and the final state is that `T` iterations have been completed, with each iteration printing a result based on the provided `a` and `b` values.

