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
        
    #State: Output State: The output state will consist of 'Bob' or 'Alice' printed for each line of input provided within the range of `t`. Specifically, 'Bob' will be printed if the sum of `a` and `b` is even, and 'Alice' will be printed if the sum is odd. The exact sequence of 'Bob' and 'Alice' depends on the input values for `a` and `b` for each iteration of the loop.
#Overall this is what the function does:The function reads a number `t` indicating the number of test cases. For each test case, it takes two non-negative integers `a` and `b` as input, checks if their sum is even or odd, and prints 'Bob' if the sum is even, otherwise prints 'Alice'. The function does not return any value.

