#State of the program right berfore the function call: The function should take two integers a and b as inputs, where 1 <= a, b <= 10^9, representing the number of coins in Alice's and Bob's wallets, respectively.
def func():
    test = int(input())
    for t in range(test):
        a, b = map(int, input().split())
        
        if a + b & 1 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: The values of `a` and `b` will be the last pair of integers read from the input during the final iteration of the loop. The value of `test` remains unchanged. The loop will print 'Bob' if the sum of `a` and `b` is even, and 'Alice' if the sum is odd, for each iteration.
#Overall this is what the function does:The function reads an integer `test` from the input, which represents the number of test cases. For each test case, it reads two integers `a` and `b` from the input, representing the number of coins in Alice's and Bob's wallets, respectively. The function then prints 'Bob' if the sum of `a` and `b` is even, and 'Alice' if the sum is odd. After processing all test cases, the function does not return any value. The final state of the program includes the last pair of integers `a` and `b` read from the input during the final iteration of the loop, and the value of `test` remains unchanged.

