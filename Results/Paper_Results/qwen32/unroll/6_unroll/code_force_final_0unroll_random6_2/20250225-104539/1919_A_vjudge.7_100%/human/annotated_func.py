#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each of the t test cases, there are two integers a and b such that 1 <= a, b <= 10^9.
def func():
    test = int(input())
    for t in range(test):
        a, b = map(int, input().split())
        
        if a + b & 1 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: t is an integer such that 1 <= t <= 1000, and for each of the t test cases, the output is either 'Bob' or 'Alice' based on whether the sum of the two integers a and b is even or odd respectively; test is an input integer.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `a` and `b`, and prints 'Bob' if the sum of `a` and `b` is even, otherwise it prints 'Alice'.

