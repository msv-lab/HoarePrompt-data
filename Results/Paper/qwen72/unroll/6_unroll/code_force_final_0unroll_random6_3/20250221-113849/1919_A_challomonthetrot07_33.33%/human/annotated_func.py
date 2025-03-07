#State of the program right berfore the function call: The function should take two parameters, a and b, which are integers such that 1 <= a, b <= 10^9. Additionally, the function should be able to handle multiple test cases, so it should either be called in a loop or modified to accept a list of tuples (a, b) as input.
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
        
    #State: The loop will execute `T` times, and for each iteration, it will read a pair of integers `a` and `b` from the input. Depending on the values of `a` and `b`, it will print either 'Alice' or 'Bob' based on the conditions specified in the loop body. The variables `a` and `b` will be updated with the new input values for each iteration, and the loop will continue until all `T` iterations are completed. After the loop finishes, the values of `a` and `b` will be the last pair of integers read from the input, and `T` will remain unchanged.
#Overall this is what the function does:The function reads an integer `T` from the input, which represents the number of test cases. For each of the `T` test cases, it reads a pair of integers `a` and `b` from the input. Based on the values of `a` and `b`, it prints either 'Alice' or 'Bob' to the console according to the following conditions: if `a` equals `b`, it prints 'Bob'; if `a` equals 1, it prints 'Alice'; if `b` equals 1, it prints 'Bob'; if `a` is odd, it prints 'Bob'; if `a` is even and `b` is odd, it prints 'Alice'; if `a` is greater than `b`, it prints 'Bob'; otherwise, it prints 'Alice'. After processing all `T` test cases, the function concludes without returning any value, and the final state of the program includes the last pair of integers read from the input for `a` and `b`, and the value of `T` remains unchanged.

