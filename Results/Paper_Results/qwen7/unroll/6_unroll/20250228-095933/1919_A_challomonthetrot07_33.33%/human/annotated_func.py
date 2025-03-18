#State of the program right berfore the function call: a and b are non-negative integers such that 1 <= a, b <= 10^9.
def func():
    T = int(input())
    for i in range(T):
        a, b = map(int, input().split())
        
        if a == b:
            print('Bob')
        elif a == 1:
            print('Alice')
        elif b == 1:
            print('Bob')
        elif a % 2 == 1:
            print('Bob')
        elif a % 2 == 0 and b % 2 == 1:
            print('Alice')
        elif a > b:
            print('Bob')
        else:
            print('Alice')
        
    #State: Output State: The output state will consist of a series of lines, each containing either 'Alice' or 'Bob', depending on the input values of `a` and `b` for each iteration of the loop. The exact sequence of 'Alice' and 'Bob' will vary based on the inputs provided during each iteration of the loop. Since the loop runs `T` times and `T` is an input from the user, the final output state cannot be precisely determined without knowing the specific values of `a` and `b` for each of the `T` iterations.
#Overall this is what the function does:The function reads an integer T from the user, indicating the number of iterations. For each iteration, it reads two integers a and b, and prints either 'Alice' or 'Bob' based on specific conditions related to the values of a and b. The final output consists of a series of lines, each containing either 'Alice' or 'Bob', depending on the input values of a and b for each iteration.

