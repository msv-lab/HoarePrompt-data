#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, a and b are integers such that 1 <= a, b <= 10^9.
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
        
    #State: The loop has finished executing t times. For each iteration, the input values a and b were read from the input, and the program printed 'Bob' if the sum of a and b was even, and 'Alice' if the sum was odd. The values of t, a, and b remain unchanged as they were input for each test case.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases, where 1 <= t <= 1000. For each test case, it reads two integers `a` and `b` from the input, where 1 <= a, b <= 10^9. It then checks if the sum of `a` and `b` is even or odd and prints 'Bob' if the sum is even, and 'Alice' if the sum is odd. After processing all `t` test cases, the function concludes without returning any value. The values of `t`, `a`, and `b` are not retained after the function execution.

