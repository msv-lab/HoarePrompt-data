#State of the program right berfore the function call: The function should take two integers a and b as inputs, where 1 <= a, b <= 10^9, representing the number of coins in Alice's and Bob's wallets, respectively.
def func():
    t = int(input())
    for i in range(t):
        a, b = list(map(int, input().split(' ')))
        
        if abs(a - b) % 2 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: The values of `a` and `b` will be the last pair of integers read from the input during the `t`-th iteration of the loop. The loop will print 'Bob' if the absolute difference between `a` and `b` is even, and 'Alice' if the absolute difference is odd, for each iteration.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads two integers `a` and `b` from the input, representing the number of coins in Alice's and Bob's wallets, respectively. The function then prints 'Bob' if the absolute difference between `a` and `b` is even, and 'Alice' if the absolute difference is odd. After processing all `t` test cases, the function completes without returning any value. The final state of the program is that the input has been fully processed and the appropriate results have been printed for each test case.

