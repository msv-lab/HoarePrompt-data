#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each of the t test cases, there are two integers a and b such that 1 ≤ a, b ≤ 10^9.
def func():
    t = int(input())
    for i in range(t):
        a, b = list(map(int, input().split(' ')))
        
        if abs(a - b) % 2 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: The loop has executed `t` times, where `t` is a specific integer between 1 and 1000. For each of the `t` test cases, two integers `a` and `b` were read from the input. The program printed "Bob" if the absolute difference between `a` and `b` was even, otherwise it printed "Alice". The variable `i` has been incremented from 0 up to `t-1` during the loop's execution.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `a` and `b`, and prints "Bob" if the absolute difference between `a` and `b` is even, otherwise it prints "Alice".

