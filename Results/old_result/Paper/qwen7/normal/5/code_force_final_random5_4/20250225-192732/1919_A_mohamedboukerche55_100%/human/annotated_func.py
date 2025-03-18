#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
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
        
    #State: After all iterations of the loop, `t` remains the same or is greater than 1, `i` is now `t-1`, `a` and `b` are the first and second integers from the last input string `s`, the sum of `a` and `b` remains even if `(a + b) % 2 == 0` is true. Otherwise, the sum of `a` and `b` is odd, `s` is the input string from the user, and no further changes occur to `a` and `b` during the loop.
#Overall this is what the function does:The function processes a series of test cases defined by a positive integer `t`. For each test case, it reads two integers `a` and `b` from the user input, checks if their sum is even, and prints either 'Bob' or 'Alice' based on the result. After processing all test cases, the function does not return any value but prints the results directly.

