#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each of the t test cases, there are two integers a and b such that 1 ≤ a, b ≤ 10^9.
def func():
    t = int(input())
    for i in range(t):
        a, b = list(map(int, input().split(' ')))
        
        if abs(a - b) % 2 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: `t` is an integer such that 1 ≤ t ≤ 1000; `a` and `b` are integers read from the input for each of the `t` test cases; the absolute difference between `a` and `b` is either even or odd for each test case; `i` has reached the value of `t`, indicating all iterations have completed.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `a` and `b`. It then determines whether the absolute difference between `a` and `b` is even or odd, printing "Bob" if it is even and "Alice" if it is odd.

