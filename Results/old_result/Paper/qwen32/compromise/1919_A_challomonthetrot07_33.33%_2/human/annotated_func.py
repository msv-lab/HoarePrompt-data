#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each of the t test cases, a and b are integers such that 1 <= a, b <= 10^9.
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
        
    #State: the sequence of 'Alice' or 'Bob' printed for each test case based on the values of `a` and `b`.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, and for each test case, it reads two integers `a` and `b`. It then prints 'Alice' or 'Bob' based on specific conditions related to the values of `a` and `b`.

