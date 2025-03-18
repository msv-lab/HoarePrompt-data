#State of the program right berfore the function call: The function should accept two integers a and b as input where 1 <= a, b <= 10^9, representing the dimensions of the rectangle. The function will be called multiple times, each time with a different set of dimensions, as part of a series of test cases.
def func():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        if a % 2 == 0 or b % 2 == 0:
            print('Yes')
        else:
            print('No')
        
    #State: The loop will execute `t` times, and for each iteration, it will read two integers `a` and `b` from the input. If either `a` or `b` is even, it will print 'Yes'. If both `a` and `b` are odd, it will print 'No'. The values of `a` and `b` will be updated with each iteration, but the value of `t` will remain unchanged.
#Overall this is what the function does:The function reads an integer `t` from the input, which represents the number of test cases. For each of the `t` test cases, it reads two integers `a` and `b` from the input, representing the dimensions of a rectangle. If either `a` or `b` is even, it prints 'Yes'. If both `a` and `b` are odd, it prints 'No'. The function does not return any value. After the function concludes, the input values `a` and `b` will have been processed `t` times, and the corresponding 'Yes' or 'No' results will have been printed for each test case. The value of `t` remains unchanged throughout the function's execution.

