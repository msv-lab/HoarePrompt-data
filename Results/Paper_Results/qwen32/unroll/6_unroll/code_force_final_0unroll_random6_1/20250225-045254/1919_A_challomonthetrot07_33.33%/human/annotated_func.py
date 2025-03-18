#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each of the t test cases, a and b are integers such that 1 ≤ a, b ≤ 10^9.
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
        
    #State: A series of printed results ('Alice' or 'Bob') corresponding to each test case. The variables `T`, `a`, and `b` will be in their final state, with `T` unchanged and `a` and `b` holding the values from the last test case.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `a` and `b`, and prints 'Alice' or 'Bob' based on specific conditions related to the values of `a` and `b`.

