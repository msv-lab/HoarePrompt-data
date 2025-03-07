#State of the program right berfore the function call: The function should take two parameters, a and b, where a and b are integers such that 1 <= a, b <= 10^9, representing the number of coins in Alice's and Bob's wallets, respectively.
def func():
    test = int(input())
    for t in range(test):
        a, b = map(int, input().split())
        
        if a + b & 1 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: `a` and `b` are integers provided by the user such that 1 <= `a`, `b` <= 10^9, `test` is greater than or equal to the number of iterations executed, and `t` is equal to `test - 1`. For each iteration, if the sum of `a` and `b` is even, the program prints 'Bob'; if the sum of `a` and `b` is odd, the program prints 'Alice'. The specific actions within the if and else parts are not detailed, but the sum of `a` and `b` retains its even or odd nature based on the user input for each iteration.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any value. It reads an integer `test` from the user, which represents the number of test cases. For each test case, it reads two integers `a` and `b` from the user, representing the number of coins in Alice's and Bob's wallets, respectively. After processing each test case, it prints 'Bob' if the sum of `a` and `b` is even, and 'Alice' if the sum is odd. The function completes after processing all test cases.

