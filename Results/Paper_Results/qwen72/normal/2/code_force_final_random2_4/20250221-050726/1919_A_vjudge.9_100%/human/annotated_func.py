#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 1000, and for each of the t test cases, a and b are integers where 1 ≤ a, b ≤ 10^9.
def func():
    t = int(input())
    for i in range(t):
        a, b = list(map(int, input().split(' ')))
        
        if abs(a - b) % 2 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: `t` is equal to the initial value, `i` is `t-1`, `a` and `b` are integers provided by user input for the last iteration. If the absolute difference between `a` and `b` is even, the condition holds true. Otherwise, the absolute difference between `a` and `b` is odd.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases (1 ≤ t ≤ 1000). For each test case, it reads two integers `a` and `b` (1 ≤ a, b ≤ 10^9). It then checks if the absolute difference between `a` and `b` is even. If it is, it prints "Bob"; otherwise, it prints "Alice". After processing all test cases, the function completes without returning any value. The final state of the program is that `t` remains unchanged, `i` is `t-1`, and `a` and `b` hold the values from the last test case.

