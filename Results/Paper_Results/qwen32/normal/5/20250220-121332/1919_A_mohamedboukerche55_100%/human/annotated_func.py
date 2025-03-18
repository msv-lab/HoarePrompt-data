#State of the program right berfore the function call: Each test case contains two integers a and b (1 ≤ a, b ≤ 10^9) representing the number of coins in Alice's and Bob's wallets, respectively. There are t (1 ≤ t ≤ 1000) such test cases.
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
        
    #State: The loop has executed `t` times, and the final output is a sequence of `t` lines, each either "Bob" or "Alice" based on the sum of `a` and `b` in each iteration.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `a` and `b` representing the number of coins in Alice's and Bob's wallets, respectively. It then prints "Bob" if the sum of `a` and `b` is even, and "Alice" if the sum is odd. This process is repeated for all `t` test cases.

