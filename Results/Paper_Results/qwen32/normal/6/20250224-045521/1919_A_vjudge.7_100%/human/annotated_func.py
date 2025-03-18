#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, a and b are integers such that 1 ≤ a, b ≤ 10^9.
def func():
    test = int(input())
    for t in range(test):
        a, b = map(int, input().split())
        
        if a + b & 1 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: `t` is an integer such that `t` equals `test`, `a` and `b` are the integers read from the input in the last iteration, `test` is greater than 0, and the sum of `a` and `b` is either even or odd. The loop has completed all `test` iterations, printing 'Bob' if the sum of `a` and `b` is even, or 'Alice' if the sum of `a` and `b` is odd for each iteration.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `a` and `b`, and prints 'Bob' if the sum of `a` and `b` is even, otherwise it prints 'Alice'.

