#State of the program right berfore the function call: The function should take two integers a and b as input, where 1 <= a, b <= 10^9, representing the number of coins in Alice's and Bob's wallets, respectively.
def func():
    test = int(input())
    for t in range(test):
        a, b = map(int, input().split())
        
        if a + b & 1 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: `a` and `b` are integers provided by the user input, `test` must be greater than or equal to the number of iterations, and `t` is `test - 1`. If the sum of `a` and `b` is even, the condition holds. If the sum of `a` and `b` is odd, the condition also holds.
#Overall this is what the function does:The function reads an integer `test` from the user input, which represents the number of test cases. For each test case, it reads two integers `a` and `b` from the user input, representing the number of coins in Alice's and Bob's wallets, respectively. The function then checks if the sum of `a` and `b` is even or odd. If the sum is even, it prints 'Bob'. If the sum is odd, it prints 'Alice'. The function does not return any values. After the function concludes, the state includes the number of test cases processed and the results printed for each test case.

