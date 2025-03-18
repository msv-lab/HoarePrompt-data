#State of the program right berfore the function call: Each test case contains two integers a and b (1 ≤ a, b ≤ 10^9) representing the number of coins in Alice's and Bob's wallets, respectively. There are t (1 ≤ t ≤ 1000) such test cases.
def func():
    t = int(input())
    for i in range(t):
        a, b = list(map(int, input().split(' ')))
        
        if abs(a - b) % 2 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: The loop will have printed "Bob" if the absolute difference between the number of coins in Alice's and Bob's wallets was even for each test case, and "Alice" if the difference was odd. The variables `a`, `b`, and `i` will have their last iteration values, and `t` will remain unchanged.
#Overall this is what the function does:The function reads the number of test cases, `t`, and for each test case, it reads two integers `a` and `b` representing the number of coins in Alice's and Bob's wallets, respectively. It then determines if the absolute difference between `a` and `b` is even or odd. If the difference is even, it prints "Bob"; if the difference is odd, it prints "Alice". This process is repeated for all `t` test cases.

