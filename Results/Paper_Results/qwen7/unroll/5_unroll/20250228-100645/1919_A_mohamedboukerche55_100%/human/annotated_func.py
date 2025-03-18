#State of the program right berfore the function call: a and b are non-negative integers such that 1 <= a, b <= 10^9.
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
        
    #State: Output State: The output state will consist of 'Bob' or 'Alice' printed for each line of input provided within the `t` iterations. Specifically, 'Bob' will be printed if the sum of `a` and `b` is even, and 'Alice' will be printed if the sum is odd.
#Overall this is what the function does:The function reads a number of test cases (`t`) from the user, followed by pairs of non-negative integers (`a` and `b`) for each test case. It then checks if the sum of `a` and `b` is even or odd and prints 'Bob' if the sum is even, and 'Alice' if the sum is odd for each test case. The function does not return any value but prints the results directly.

