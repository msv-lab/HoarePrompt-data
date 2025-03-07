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
        
    #State: Output State: The value of `a` and `b` will be updated based on the last input provided before the loop completes. The variable `t` will remain unchanged from its initial value, and `i` will be equal to `t - 1`. If the sum of `a` and `b` from the last input is even, the output will be 'Bob' printed `t` times. If the sum is odd, the output will be 'Alice' printed `t` times.
    #
    #This means that after all iterations of the loop have finished, the final values of `a` and `b` will reflect the most recent input provided, while `t` retains its original value, and `i` is set to `t - 1`. The loop's output will consist of 'Bob' or 'Alice' repeated `t` times based on whether the sum of `a` and `b` from the last input is even or odd, respectively.
#Overall this is what the function does:The function reads a number of test cases (`t`) and for each case, it takes two non-negative integers (`a` and `b`). It then checks if the sum of `a` and `b` is even or odd. Based on this check, it prints 'Bob' or 'Alice' respectively, for each test case. After processing all test cases, the function does not return any value but prints 'Bob' or 'Alice' a total of `t` times.

