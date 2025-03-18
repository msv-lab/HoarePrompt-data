#State of the program right berfore the function call: Each test case contains two integers a and b (1 ≤ a, b ≤ 10^9) representing the number of coins in Alice's and Bob's wallets, respectively. There are t (1 ≤ t ≤ 1000) such test cases.
def func():
    test = int(input())
    for t in range(test):
        a, b = map(int, input().split())
        
        if a + b & 1 == 0:
            print('Bob')
        else:
            print('Alice')
        
    #State: `test` is 0, `t` is equal to `test - 1` (the last iteration index), and all test cases have been processed. For each test case, the program has printed either 'Bob' or 'Alice' based on whether the sum of `a` and `b` was even or odd.
#Overall this is what the function does:The function processes `t` test cases, each consisting of two integers `a` and `b` representing the number of coins in Alice's and Bob's wallets, respectively. For each test case, it prints 'Bob' if the sum of `a` and `b` is even, and 'Alice' if the sum is odd.

