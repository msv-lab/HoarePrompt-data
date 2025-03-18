#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each of the t test cases, a and b are integers such that 1 ≤ a, b ≤ 10^9.
def func():
    t = int(input())
    for i in range(t):
        a, b = list(map(int, input().split(' ')))
        
        if abs(a - b) % 2 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: `t` is an integer read from input such that 1 ≤ `t` ≤ 1000; `a` and `b` are the last pair of integers read from input; the absolute difference between `a` and `b` is either even or odd; `i` has reached the value of `t` and the loop has terminated. Regardless of whether the absolute difference between `a` and `b` is even or odd, `i` has completed all `t` iterations.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `a` and `b`. It then prints "Bob" if the absolute difference between `a` and `b` is even, otherwise it prints "Alice".

