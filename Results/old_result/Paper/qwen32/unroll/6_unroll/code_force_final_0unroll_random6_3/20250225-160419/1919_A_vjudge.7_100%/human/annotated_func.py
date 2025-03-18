#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each of the t test cases, a and b are integers such that 1 ≤ a, b ≤ 10^9.
def func():
    test = int(input())
    for t in range(test):
        a, b = map(int, input().split())
        
        if a + b & 1 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: After executing all iterations, the program will have printed either 'Bob' or 'Alice' for each of the `test` test cases based on whether the sum of `a` and `b` is even or odd, respectively. The values of `a`, `b`, and `t` will reflect the last iteration's values, and `test` will remain unchanged.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `a` and `b`, and prints 'Bob' if the sum of `a` and `b` is even, otherwise it prints 'Alice'. After processing all test cases, the function concludes without returning any value.

