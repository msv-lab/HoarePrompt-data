#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each of the t test cases, a and b are integers such that 1 ≤ a, b ≤ 10^9.
def func():
    t = int(input())
    for i in range(t):
        s = input()
        
        a = int(list(s.split())[0])
        
        b = int(list(s.split())[1])
        
        if (a + b) % 2 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: For each of the `t` test cases, the program will output either 'Bob' or 'Alice' based on whether the sum of `a` and `b` is even or odd. The variable `t` remains unchanged, and `a` and `b` are re-assigned for each iteration but do not persist after the loop.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `a` and `b`, and prints 'Bob' if the sum of `a` and `b` is even, otherwise it prints 'Alice'. The values of `a` and `b` do not persist after each test case.

