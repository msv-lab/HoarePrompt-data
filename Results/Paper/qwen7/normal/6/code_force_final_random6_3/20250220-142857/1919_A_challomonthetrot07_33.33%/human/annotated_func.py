#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
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
        
    #State: T is a positive integer such that 1 ≤ T ≤ 1000, i is equal to T - 1, a is the first integer input converted to an integer, b is the second integer input converted to an integer. The values of T and a remain unchanged regardless of the loop iterations, and i increments by 1 with each iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer `T` and pairs of positive integers `a` and `b`. For each test case, it determines and prints whether 'Alice' or 'Bob' wins based on specific conditions involving `a` and `b`. The final state of the program includes printed outcomes for all test cases, with `T` remaining unchanged and `i` being updated to `T - 1` after processing all cases.

